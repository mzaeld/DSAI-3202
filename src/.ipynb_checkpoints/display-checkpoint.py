
import sys
import os
import time
import threading
from src.sync_utils import lock
from src.sensor import latest_temperatures
from src.processor import temperature_averages

def initialize_display():
    """Prints the initial display layout."""
    print("Current temperatures:")
    print("Latest Temperatures:", end=" ")
    for i in range(3):
        print(f"Sensor {i}: --°C", end=" ")
    print()
    for i in range(3):
        print(f"Sensor {i} Average: --°C")

def update_display():
    """Updates the console display with latest readings."""
    while True:
        with lock:
            # Debugging - Check if data is actually updating
            print(f"DEBUG - latest_temperatures: {latest_temperatures}")
            print(f"DEBUG - temperature_averages: {temperature_averages}")

            os.system("cls" if os.name == "nt" else "clear")  # Cross-platform clear screen
            
            print("Current temperatures:")
            print("Latest Temperatures:", end=" ")
            for i in range(3):
                temp = latest_temperatures.get(i, "--")
                print(f"Sensor {i}: {temp}°C", end=" ")
            print("\n")
            for i in range(3):
                avg = temperature_averages.get(i, "--")
                print(f"Sensor {i} Average: {avg:.2f}°C" if isinstance(avg, (int, float)) else f"Sensor {i} Average: --°C")

        time.sleep(5)  # Refresh every 5 seconds


