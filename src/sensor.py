
import random
import threading
import time
from src.sync_utils import lock

latest_temperatures = {}

def simulate_sensor(sensor_id):
    """Simulates a sensor reading and updates global temperatures."""
    while True:
        temp = random.randint(15, 40)
        with lock:
            latest_temperatures[sensor_id] = temp
        time.sleep(1)  # Update every second

