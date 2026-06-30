"""
Configuration settings for RevXcel application
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Database configuration
DATABASE_PATH = BASE_DIR / "revxcel.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Data file paths
DATA_DIR = BASE_DIR / "data"
SALES_DATA_PROCESSED = DATA_DIR / "sales_data_processed.csv"
SALES_DATA_ML_READY = DATA_DIR / "sales_data_ml_ready.csv"
CUSTOMER_METRICS = DATA_DIR / "customer_metrics.csv"
CAMPAIGN_DATA = DATA_DIR / "campaign_data.csv"

# ML Models directory
MODELS_DIR = BASE_DIR / "models" / "saved_models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Reports directory
REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Secret key for session management (change in production)
SECRET_KEY = os.environ.get("REVXCEL_SECRET_KEY", "dev-secret-key-change-in-production")

# User roles
ROLES = {
    "DEVELOPER": "Developer",
    "MARKETING_USER": "MarketingUser",
    "ONLINE_SHOP": "OnlineShop"
}

# Default admin credentials (change in production)
DEFAULT_ADMIN_USERNAME = "admin"
DEFAULT_ADMIN_PASSWORD = "admin123"  # Change this in production
DEFAULT_ADMIN_EMAIL = "admin@revxcel.com"

