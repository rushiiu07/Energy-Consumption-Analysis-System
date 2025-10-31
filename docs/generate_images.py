import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime, timedelta

def create_system_overview():
    # Create system overview diagram
    plt.figure(figsize=(12, 8))
    plt.title('Energy Consumption Analysis System Overview')
    
    components = ['Sensors', 'Data\nCollector', 'Energy\nAnalyzer', 'Visualizer', 'Alert\nSystem', 'Reports']
    x = np.arange(len(components))
    y = [0] * len(components)
    
    plt.plot(x, y, 'bo-')
    plt.xticks(x, components)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('docs/images/system_overview.png', bbox_inches='tight', dpi=300)
    plt.close()

def create_power_consumption_graph():
    # Create sample power consumption graph
    plt.figure(figsize=(10, 6))
    
    # Generate sample data
    dates = [datetime.now() + timedelta(hours=x) for x in range(24)]
    power = np.random.normal(1000, 100, 24) + np.sin(np.arange(24) * np.pi/12) * 50
    
    plt.plot(dates, power, 'g-', label='Power Consumption')
    plt.fill_between(dates, power-50, power+50, alpha=0.3, color='green')
    
    plt.title('24-Hour Power Consumption')
    plt.xlabel('Time')
    plt.ylabel('Power (kW)')
    plt.grid(True)
    plt.legend()
    
    plt.savefig('docs/images/power_consumption.png', bbox_inches='tight', dpi=300)
    plt.close()

def create_efficiency_trends():
    # Create efficiency trends visualization
    plt.figure(figsize=(10, 6))
    
    # Generate sample data
    days = 30
    efficiency = np.random.normal(0.85, 0.05, days) + np.sin(np.arange(days) * np.pi/15) * 0.02
    
    plt.plot(range(days), efficiency * 100, 'b-', label='Efficiency')
    plt.axhline(y=85, color='r', linestyle='--', label='Target Efficiency')
    
    plt.title('Monthly Efficiency Trends')
    plt.xlabel('Days')
    plt.ylabel('Efficiency (%)')
    plt.grid(True)
    plt.legend()
    
    plt.savefig('docs/images/efficiency_trends.png', bbox_inches='tight', dpi=300)
    plt.close()

def create_monitoring_interface():
    # Create a mock monitoring interface
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Sample data
    times = np.arange(100)
    power = np.random.normal(1000, 50, 100)
    temp = np.random.normal(75, 5, 100)
    flow = np.random.normal(150, 10, 100)
    efficiency = np.random.normal(0.85, 0.02, 100)
    
    # Power consumption
    ax1.plot(times, power, 'r-')
    ax1.set_title('Power Consumption')
    ax1.grid(True)
    
    # Temperature
    ax2.plot(times, temp, 'g-')
    ax2.set_title('Temperature')
    ax2.grid(True)
    
    # Flow rate
    ax3.plot(times, flow, 'b-')
    ax3.set_title('Flow Rate')
    ax3.grid(True)
    
    # Efficiency
    ax4.plot(times, efficiency, 'y-')
    ax4.set_title('Efficiency')
    ax4.grid(True)
    
    plt.tight_layout()
    plt.savefig('docs/images/monitoring.png', bbox_inches='tight', dpi=300)
    plt.close()

def create_component_structure():
    # Create component structure diagram
    plt.figure(figsize=(12, 8))
    
    components = ['Data\nCollection', 'Processing', 'Analysis', 'Visualization', 'Reporting']
    x = np.arange(len(components))
    y = [0] * len(components)
    
    plt.plot(x, y, 'ro-', linewidth=2)
    plt.xticks(x, components)
    
    # Add component descriptions
    for i, comp in enumerate(components):
        plt.annotate(f'Component {i+1}',
                    xy=(i, 0), xytext=(0, 30),
                    textcoords='offset points',
                    ha='center',
                    va='bottom',
                    bbox=dict(boxstyle='round,pad=0.5',
                            fc='yellow',
                            alpha=0.5),
                    arrowprops=dict(arrowstyle='->'))
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title('System Component Structure')
    plt.savefig('docs/images/component_structure.png', bbox_inches='tight', dpi=300)
    plt.close()

def create_dashboard():
    # Create a mock dashboard
    fig = plt.figure(figsize=(15, 10))
    gs = fig.add_gridspec(3, 3)
    
    # Power consumption trend
    ax1 = fig.add_subplot(gs[0, :])
    times = np.arange(100)
    power = np.random.normal(1000, 50, 100)
    ax1.plot(times, power, 'r-')
    ax1.set_title('Power Consumption Trend')
    ax1.grid(True)
    
    # Efficiency gauge
    ax2 = fig.add_subplot(gs[1:, 0])
    efficiency = 0.85
    ax2.pie([efficiency, 1-efficiency], colors=['g', 'lightgray'])
    ax2.set_title(f'Efficiency: {efficiency:.1%}')
    
    # Temperature heatmap
    ax3 = fig.add_subplot(gs[1:, 1])
    temp_data = np.random.normal(75, 5, (10, 10))
    sns.heatmap(temp_data, ax=ax3, cmap='YlOrRd')
    ax3.set_title('Temperature Distribution')
    
    # Alert history
    ax4 = fig.add_subplot(gs[1:, 2])
    alerts = [3, 1, 4, 1, 5]
    ax4.bar(range(len(alerts)), alerts)
    ax4.set_title('Alert History')
    
    plt.tight_layout()
    plt.savefig('docs/images/dashboard.png', bbox_inches='tight', dpi=300)
    plt.close()

if __name__ == "__main__":
    # Create all visualizations
    create_system_overview()
    create_power_consumption_graph()
    create_efficiency_trends()
    create_monitoring_interface()
    create_component_structure()
    create_dashboard()