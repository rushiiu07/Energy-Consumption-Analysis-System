"""
Main application for Energy Consumption Analysis
"""
import time
from datetime import datetime
import os
from data_collector import DataCollector
from energy_analyzer import EnergyAnalyzer
from visualizer import EnergyVisualizer
from config import SENSOR_CONFIG, ALERT_THRESHOLDS, REPORT_CONFIG

class EnergyMonitoringSystem:
    def __init__(self):
        # Create reports directory if it doesn't exist
        if not os.path.exists('reports'):
            os.makedirs('reports')

        # Initialize components
        self.collector = DataCollector(SENSOR_CONFIG)
        self.analyzer = EnergyAnalyzer(ALERT_THRESHOLDS)
        self.visualizer = EnergyVisualizer()
        
        # Initialize data storage
        self.daily_data = []
        self.start_time = datetime.now()

    def run(self):
        """
        Main execution loop
        """
        print("Starting Energy Monitoring System...")
        
        try:
            while True:
                # Collect data
                raw_data = self.collector.collect_data()
                
                # Process and analyze data
                processed_data = self.analyzer.process_data(raw_data)
                self.daily_data.append(processed_data)
                
                # Check for alerts
                alerts = self.analyzer.check_alerts(processed_data)
                if alerts:
                    print("\nALERTS:")
                    for alert in alerts:
                        print(f"- {alert}")
                
                # Generate daily report if needed
                current_time = datetime.now()
                if (current_time - self.start_time).days >= 1:
                    self.generate_daily_report()
                    self.start_time = current_time
                    self.daily_data = []
                
                # Wait for next collection interval
                time.sleep(SENSOR_CONFIG['data_collection_interval'])
                
        except KeyboardInterrupt:
            print("\nShutting down Energy Monitoring System...")
            self.generate_daily_report()  # Generate final report before shutting down

    def generate_daily_report(self):
        """
        Generate and save daily report with visualizations
        """
        print("\nGenerating daily report...")
        
        # Generate data summary
        daily_summary = self.analyzer.generate_daily_report()
        
        # Create visualizations
        power_plot = self.visualizer.plot_power_consumption(self.daily_data)
        self.visualizer.save_plots(power_plot, f'power_consumption_{datetime.now().strftime("%Y%m%d")}')
        
        efficiency_plot = self.visualizer.plot_efficiency_trends(self.daily_data)
        self.visualizer.save_plots(efficiency_plot, f'efficiency_trends_{datetime.now().strftime("%Y%m%d")}')
        
        # Save summary to CSV
        daily_summary.to_csv(f'reports/daily_summary_{datetime.now().strftime("%Y%m%d")}.csv')
        
        print("Daily report generated successfully!")

if __name__ == "__main__":
    system = EnergyMonitoringSystem()
    system.run()