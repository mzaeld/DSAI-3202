import threading
import random
import time
from queue import Queue

# Shared Data Structures
latest_temperatures = {}
temperature_averages = {}
temperature_queue = Queue()
lock = threading.RLock()
condition = threading.Condition(lock)

# Sensor Simulation
def simulate_sensor(sensor_id):
    global latest_temperatures
    while True:
        temperature = random.randint(15, 40)
        with lock:
            latest_temperatures[sensor_id] = temperature
            temperature_queue.put((sensor_id, temperature))
        time.sleep(1)

# Data Processing
def process_temperatures():
    sensor_data = {}
    while True:
        with condition:
            while temperature_queue.empty():
                condition.wait()
            sensor_id, temperature = temperature_queue.get()
            if sensor_id not in sensor_data:
                sensor_data[sensor_id] = []
            sensor_data[sensor_id].append(temperature)
            if len(sensor_data[sensor_id]) > 10:
                sensor_data[sensor_id].pop(0)  # Keep only the last 10 readings
            with lock:
                temperature_averages[sensor_id] = sum(sensor_data[sensor_id]) / len(sensor_data[sensor_id])
        time.sleep(5)

# Display Logic
def initialize_display():
    print("Current temperatures:")
    print("Latest Temperatures:", " ".join(f"Sensor {i}: --°C" for i in range(3)))
    print(" ".join(f"Sensor {i} Average: --°C" for i in range(3)))

def update_display():
    while True:
        with lock:
            print("\r", end="")
            print("Latest Temperatures:", " ".join(f"Sensor {i}: {latest_temperatures.get(i, '--')}°C" for i in range(3)), end=" | ")
            print(" ".join(f"Sensor {i} Average: {temperature_averages.get(i, '--'):.2f}°C" for i in range(3)), end="", flush=True)
        time.sleep(5)

# Main Program
def main():
    global latest_temperatures, temperature_averages
    for i in range(3):
        threading.Thread(target=simulate_sensor, args=(i,), daemon=True).start()
    threading.Thread(target=process_temperatures, daemon=True).start()
    threading.Thread(target=update_display, daemon=True).start()
    
    initialize_display()
    while True:
        time.sleep(1)  # Keep the main thread running