#!/usr/bin/env python3
import threading
import time
from collections import deque
from src.sync_utils import queue_condition

temperature_averages = {}
data_queue = {}

def process_temperatures(sensor_id):
    """Computes the moving average of temperature readings."""
    data_queue[sensor_id] = deque(maxlen=10)  # Store last 10 readings
    
    while True:
        with queue_condition:
            queue_condition.wait()  # Wait for new data
            if data_queue[sensor_id]:
                temperature_averages[sensor_id] = sum(data_queue[sensor_id]) / len(data_queue[sensor_id])

def add_to_queue(sensor_id, value):
    """Adds sensor data to queue and notifies the processor thread."""
    with queue_condition:
        data_queue[sensor_id].append(value)
        queue_condition.notify()

