"""
Module for collecting real-time energy consumption data from sensors
"""
import time
import random
from datetime import datetime
from typing import Dict, List

class DataCollector:
    def __init__(self, sensor_config: Dict):
        self.sensor_config = sensor_config
        self.sensor_data = {}

    def read_sensor(self, sensor_id: str) -> float:
        """
        Simulate reading data from a sensor
        In production, this would interface with actual sensors
        """
        if sensor_id.startswith('PM'):  # Power meter
            return random.uniform(800, 1200)  # kW
        elif sensor_id.startswith('TMP'):  # Temperature
            return random.uniform(60, 90)  # Celsius
        elif sensor_id.startswith('FM'):  # Flow meter
            return random.uniform(100, 200)  # m³/h
        return 0.0

    def collect_data(self) -> Dict:
        """
        Collect data from all configured sensors
        """
        timestamp = datetime.now()
        readings = {
            'timestamp': timestamp,
            'readings': {}
        }

        for sensor_type, sensors in self.sensor_config['sensors'].items():
            readings['readings'][sensor_type] = {}
            for sensor_id in sensors:
                readings['readings'][sensor_type][sensor_id] = self.read_sensor(sensor_id)

        return readings

    def start_collection(self, interval: int):
        """
        Start continuous data collection
        """
        while True:
            data = self.collect_data()
            print(f"Collected data at {data['timestamp']}")
            print(data['readings'])
            time.sleep(interval)

if __name__ == "__main__":
    from config import SENSOR_CONFIG
    collector = DataCollector(SENSOR_CONFIG)
    collector.start_collection(SENSOR_CONFIG['data_collection_interval'])