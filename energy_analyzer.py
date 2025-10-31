"""
Module for processing and analyzing energy consumption data
"""
from typing import Dict, List
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class EnergyAnalyzer:
    def __init__(self, alert_thresholds: Dict):
        self.alert_thresholds = alert_thresholds
        self.data_cache = []

    def process_data(self, data: Dict) -> Dict:
        """
        Process raw sensor data and calculate key metrics
        """
        processed_data = {
            'timestamp': data['timestamp'],
            'metrics': {}
        }

        # Calculate total power consumption
        power_readings = data['readings']['power_meter'].values()
        total_power = sum(power_readings)
        avg_power = total_power / len(power_readings)

        # Calculate average temperature
        temp_readings = data['readings']['temperature'].values()
        avg_temp = sum(temp_readings) / len(temp_readings)

        # Calculate energy efficiency
        flow_readings = data['readings']['flow_meter'].values()
        total_flow = sum(flow_readings)
        efficiency = self.calculate_efficiency(total_power, total_flow)

        processed_data['metrics'] = {
            'total_power_consumption': total_power,
            'average_power': avg_power,
            'average_temperature': avg_temp,
            'total_flow': total_flow,
            'efficiency': efficiency
        }

        return processed_data

    def calculate_efficiency(self, power: float, flow: float) -> float:
        """
        Calculate energy efficiency based on power consumption and flow rate
        """
        # Simplified efficiency calculation
        # In real scenarios, this would involve more complex thermodynamic calculations
        if flow == 0:
            return 0
        return (flow * 0.7) / power  # 0.7 is a theoretical conversion factor

    def check_alerts(self, processed_data: Dict) -> List[str]:
        """
        Check for any threshold violations and generate alerts
        """
        alerts = []
        metrics = processed_data['metrics']

        if metrics['total_power_consumption'] > self.alert_thresholds['power_consumption_high']:
            alerts.append(f"High power consumption alert: {metrics['total_power_consumption']} kW")

        if metrics['average_temperature'] > self.alert_thresholds['temperature_high']:
            alerts.append(f"High temperature alert: {metrics['average_temperature']} °C")

        if metrics['efficiency'] < self.alert_thresholds['efficiency_low']:
            alerts.append(f"Low efficiency alert: {metrics['efficiency']:.2%}")

        return alerts

    def generate_daily_report(self) -> pd.DataFrame:
        """
        Generate a daily summary report of energy consumption
        """
        df = pd.DataFrame(self.data_cache)
        daily_summary = {
            'total_energy_consumed': df['total_power_consumption'].sum() * (5/60),  # kWh
            'average_efficiency': df['efficiency'].mean(),
            'peak_power': df['total_power_consumption'].max(),
            'total_cost': (df['total_power_consumption'].sum() * (5/60) * 0.12)  # Assuming $0.12 per kWh
        }
        return pd.DataFrame([daily_summary])

if __name__ == "__main__":
    from config import ALERT_THRESHOLDS
    analyzer = EnergyAnalyzer(ALERT_THRESHOLDS)
    # Test with sample data
    sample_data = {
        'timestamp': datetime.now(),
        'readings': {
            'power_meter': {'PM001': 950, 'PM002': 1100, 'PM003': 880},
            'temperature': {'TMP001': 75, 'TMP002': 78, 'TMP003': 72},
            'flow_meter': {'FM001': 150, 'FM002': 160, 'FM003': 140}
        }
    }
    processed = analyzer.process_data(sample_data)
    alerts = analyzer.check_alerts(processed)
    print("Processed Data:", processed)
    print("Alerts:", alerts)