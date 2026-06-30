# RevXcel - Smart Marketing Intelligence System

A production-ready marketing intelligence platform that integrates big data analysis, machine learning, and interactive dashboards to provide actionable insights for marketing and sales teams.

## Features

- **Interactive Dashboard**: Real-time KPIs including ROI, CLV, Conversion Rate, and Total Revenue
- **Campaign Analysis**: Comprehensive campaign performance metrics and ROI analysis
- **Customer Segmentation**: ML-powered customer segmentation using RFM analysis and predictive models
- **Report Generation**: Export insights to PDF and CSV formats
- **Role-Based Access**: Support for Developer, Marketing User, and Online Shop roles

## Technology Stack

- **Frontend**: Plotly Dash with Bootstrap components
- **Backend**: Python with SQLAlchemy
- **Machine Learning**: XGBoost, LightGBM, Scikit-learn (KMeans, Random Forest)
- **Database**: SQLite
- **Data Processing**: Pandas, NumPy

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd RevXcel
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Ensure data files are in the `data/` directory:
   - `sales_data_processed.csv`
   - `sales_data_ml_ready.csv`
   - `customer_metrics.csv`
   - `campaign_data.csv`

5. Run the application:
```bash
python app.py
```

6. Access the application at `http://localhost:8050`

## Default Login Credentials

- **Username**: admin
- **Password**: admin123
- **Role**: Developer

**⚠️ Important**: Change the default admin password in production!

## Project Structure

```
RevXcel/
├── app.py                 # Main Dash application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── models/
│   ├── database.py        # Database models
│   └── ml_models.py       # ML model training and prediction
├── utils/
│   ├── data_loader.py     # Data loading utilities
│   ├── kpi_calculator.py  # KPI calculations
│   └── auth.py            # Authentication logic
├── components/
│   ├── dashboard.py       # Main dashboard
│   ├── campaign_analysis.py # Campaign analysis page
│   ├── customer_segmentation.py # ML predictions page
│   └── reports.py         # Report generation
├── assets/
│   └── style.css          # Custom CSS
└── data/                  # Data files
```

## Usage

1. **Login**: Use your credentials to access the system
2. **Dashboard**: View overall KPIs and performance metrics
3. **Campaign Analysis**: Analyze campaign performance by channel and date range
4. **Customer Segmentation**: View customer segments and run ML predictions
5. **Reports**: Generate and download reports in PDF or CSV format

## Development

This project follows the YAGNI (You Aren't Gonna Need It) principle, focusing on essential features for production readiness.

## License

Academic Project - Al-Baha University

