import random
import time
import threading

# Global dictionary to store latest temperatures
latest_temperatures = {}

def simulate_sensor(sensor_id):
    """Simulates temperature readings from a sensor and updates the global dictionary."""
    while True:
        temperature = random.randint(15, 40)  # Generate random temperature
        latest_temperatures[sensor_id] = temperature  # Update dictionary
        time.sleep(1)  # Wait for 1 second before next reading

# Example: Start simulation for multiple sensors
sensor_ids = ["sensor_1", "sensor_2"]
for sensor_id in sensor_ids:
    threading.Thread(target=simulate_sensor, args=(sensor_id,), daemon=True).start()

# The main thread can continue with other tasks or keep running
while True:
    print(latest_temperatures)  # Print latest readings
    time.sleep(5)  # Print every 5 seconds
    
    