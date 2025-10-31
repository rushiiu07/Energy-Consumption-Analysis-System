"""
Configuration settings for the Energy Consumption Analysis system
"""

# Database Configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'database': 'petrochemical_plant',
    'user': 'your_username',
    'password': 'your_password'
}

# Sensor Data Configuration
SENSOR_CONFIG = {
    'data_collection_interval': 300,  # in seconds
    'sensors': {
        'power_meter': ['PM001', 'PM002', 'PM003'],
        'temperature': ['TMP001', 'TMP002', 'TMP003'],
        'flow_meter': ['FM001', 'FM002', 'FM003']
    }
}

# Alert Thresholds
ALERT_THRESHOLDS = {
    'power_consumption_high': 1000,  # kW
    'temperature_high': 80,  # Celsius
    'efficiency_low': 0.85  # 85% efficiency threshold
}

# Reporting Configuration
REPORT_CONFIG = {
    'report_interval': 'daily',
    'email_recipients': ['manager@company.com'],
    'report_format': 'pdf'
}