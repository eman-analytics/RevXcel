"""
Main RevXcel Dash Application
"""
import dash
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import os

# Import components
from components.dashboard import create_dashboard_layout
from components.campaign_analysis import create_campaign_analysis_layout
from components.customer_segmentation import create_customer_segmentation_layout
from components.reports import create_reports_layout

# Import utilities
from utils.auth import authenticate_user, get_user_by_id, check_role_access
from models.database import init_db
from models.ml_models import ml_models
import config

# Initialize database
init_db()

# Initialize ML models
try:
    ml_models.initialize_models()
except Exception as e:
    print(f"Warning: Could not initialize ML models: {e}")

# Initialize Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

app.title = "RevXcel - Marketing Intelligence System"

# Server for session management
server = app.server
server.secret_key = config.SECRET_KEY


def create_login_layout():
    """Create login page layout with improved alignment and height"""
    return html.Div(
        [
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Card(
                                    [
                                        dbc.CardHeader(
                                            "RevXcel Login", className="text-center"
                                        ),
                                        dbc.CardBody(
                                            [
                                                dbc.Input(
                                                    id="login-username",
                                                    type="text",
                                                    placeholder="Username",
                                                    className="mb-3"
                                                ),
                                                dbc.Input(
                                                    id="login-password",
                                                    type="password",
                                                    placeholder="Password",
                                                    className="mb-3"
                                                ),
                                                dbc.Button(
                                                    "Login",
                                                    id="login-btn",
                                                    color="primary",
                                                    className="w-100 mb-2"
                                                ),
                                                html.Div(id="login-status"),
                                                html.Hr(),
                                                html.P(
                                                    "Default credentials: admin / admin123",
                                                    className="text-muted text-center small"
                                                )
                                            ]
                                        )
                                    ],
                                    className="shadow"
                                ),
                                md=4, xs=12, className="offset-md-4"
                            )
                        ],
                        className="justify-content-center align-items-center",
                        style={"minHeight": "100vh"},
                    )
                ],
                fluid=True
            )
        ],
        style={"minHeight": "100vh", "backgroundColor": "#f8f9fa", "display": "flex", "alignItems": "center"}
    )


def create_navbar(user=None):
    """Create navigation navbar"""
    if user is None:
        return None

    nav_items = [
        dbc.NavItem(dbc.NavLink("Dashboard", href="/dashboard", active="exact")),
        dbc.NavItem(dbc.NavLink("Campaign Analysis", href="/campaigns", active="exact")),
        dbc.NavItem(dbc.NavLink("Customer Segmentation", href="/segmentation", active="exact")),
        dbc.NavItem(dbc.NavLink("Reports", href="/reports", active="exact")),
    ]

    # Add admin features for Developer role
    if user and user.role == config.ROLES["DEVELOPER"]:
        nav_items.append(dbc.NavItem(dbc.NavLink("Admin", href="/admin", active="exact")))

    return dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand("RevXcel", href="/dashboard"),
                dbc.Nav(
                    nav_items,
                    navbar=True,
                    pills=True,
                    className="ms-auto"
                ),
            ],
            fluid=True
        ),
        color="primary",
        dark=True,
        className="mb-4"
    )


def create_main_layout():
    """Create main application layout with proper structure to avoid overflow"""
    return html.Div(
        [
            dcc.Location(id="url", refresh=False),
            dcc.Store(id="user-store", data=None),  # Store user session
            html.Div(id="page-content", style={"minHeight": "90vh"})
        ],
        style={"backgroundColor": "#f8f9fa", "minHeight": "100vh"}
    )


app.layout = create_main_layout()


@callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    State("user-store", "data")
)
def display_page(pathname, user_data):
    """Display page based on URL and authentication"""
    # Simple session check (in production, use proper session management)
    user = None
    if user_data:
        user = get_user_by_id(user_data.get("id"))

    # If not logged in and not on login page, redirect to login
    if not user and pathname != "/login" and pathname != "/":
        return create_login_layout()

    # Login page
    if pathname == "/login" or pathname == "/":
        if user:
            # Already logged in, show dashboard (URL will be updated by login callback if needed)
            navbar = create_navbar(user)
            return html.Div(
                [
                    navbar,
                    dbc.Container(
                        create_dashboard_layout(),
                        fluid=True,
                        className="pt-4"
                    )
                ],
                style={"minHeight": "100vh", "backgroundColor": "#f8f9fa"}
            )
        return create_login_layout()

    # Authenticated pages
    navbar = create_navbar(user)

    if pathname == "/dashboard":
        content = create_dashboard_layout()
    elif pathname == "/campaigns":
        content = create_campaign_analysis_layout()
    elif pathname == "/segmentation":
        content = create_customer_segmentation_layout()
    elif pathname == "/reports":
        content = create_reports_layout()
    else:
        content = html.Div([
            html.H2("404 - Page Not Found", className="text-danger"),
            html.P("The page you're looking for doesn't exist.")
        ], className="text-center py-5")

    return html.Div(
        [
            navbar,
            dbc.Container(content, fluid=True, className="pt-4")
        ],
        style={"minHeight": "100vh", "backgroundColor": "#f8f9fa"}
    )


@callback(
    Output("login-status", "children"),
    Output("url", "pathname"),
    Output("user-store", "data"),
    Input("login-btn", "n_clicks"),
    State("login-username", "value"),
    State("login-password", "value"),
    prevent_initial_call=True
)
def login(n_clicks, username, password):
    """Handle user login"""
    if n_clicks is None:
        return "", dash.no_update, None

    if not username or not password:
        return dbc.Alert("Please enter username and password", color="danger"), dash.no_update, None

    user = authenticate_user(username, password)

    if user:
        user_data = {"id": user.id, "username": user.username, "role": user.role}
        return dbc.Alert("Login successful! Redirecting...", color="success"), "/dashboard", user_data
    else:
        return dbc.Alert("Invalid username or password", color="danger"), "/login", None


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)

