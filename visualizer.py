"""
Module for creating visualizations of energy consumption data
"""
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd
from typing import Dict, List

class EnergyVisualizer:
    def __init__(self):
        self.plt = plt
        self.plt.style.use('seaborn')

    def plot_power_consumption(self, data: List[Dict]):
        """
        Create a line plot of power consumption over time
        """
        df = pd.DataFrame(data)
        plt.figure(figsize=(12, 6))
        plt.plot(df['timestamp'], df['total_power_consumption'], label='Total Power')
        plt.title('Power Consumption Over Time')
        plt.xlabel('Time')
        plt.ylabel('Power Consumption (kW)')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt

    def plot_efficiency_trends(self, data: List[Dict]):
        """
        Create a combined plot of efficiency metrics
        """
        df = pd.DataFrame(data)
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

        # Efficiency over time
        ax1.plot(df['timestamp'], df['efficiency'], label='Efficiency', color='green')
        ax1.set_title('Energy Efficiency Over Time')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Efficiency')
        ax1.grid(True)
        ax1.legend()

        # Temperature correlation
        ax2.scatter(df['average_temperature'], df['efficiency'], alpha=0.5)
        ax2.set_title('Efficiency vs Temperature')
        ax2.set_xlabel('Temperature (°C)')
        ax2.set_ylabel('Efficiency')
        ax2.grid(True)

        plt.tight_layout()
        return plt

    def create_daily_summary_plot(self, daily_data: pd.DataFrame):
        """
        Create a summary plot of daily energy metrics
        """
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Total Energy Consumed
        axes[0, 0].bar(daily_data.index, daily_data['total_energy_consumed'])
        axes[0, 0].set_title('Total Energy Consumed (kWh)')
        axes[0, 0].tick_params(axis='x', rotation=45)

        # Average Efficiency
        axes[0, 1].bar(daily_data.index, daily_data['average_efficiency'])
        axes[0, 1].set_title('Average Efficiency')
        axes[0, 1].tick_params(axis='x', rotation=45)

        # Peak Power
        axes[1, 0].bar(daily_data.index, daily_data['peak_power'])
        axes[1, 0].set_title('Peak Power (kW)')
        axes[1, 0].tick_params(axis='x', rotation=45)

        # Total Cost
        axes[1, 1].bar(daily_data.index, daily_data['total_cost'])
        axes[1, 1].set_title('Total Cost ($)')
        axes[1, 1].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        return plt

    def save_plots(self, plt, filename: str):
        """
        Save the plot to a file
        """
        plt.savefig(f'reports/{filename}.png')
        plt.close()

if __name__ == "__main__":
    # Test visualization with sample data
    visualizer = EnergyVisualizer()
    
    # Generate sample data
    sample_data = []
    base_time = datetime.now()
    for i in range(24):
        sample_data.append({
            'timestamp': base_time + timedelta(hours=i),
            'total_power_consumption': 900 + 100 * np.sin(i/4),
            'efficiency': 0.85 + 0.05 * np.sin(i/6),
            'average_temperature': 75 + 5 * np.sin(i/8)
        })
    
    # Create and save plots
    power_plot = visualizer.plot_power_consumption(sample_data)
    visualizer.save_plots(power_plot, 'power_consumption')
    
    efficiency_plot = visualizer.plot_efficiency_trends(sample_data)
    visualizer.save_plots(efficiency_plot, 'efficiency_trends')