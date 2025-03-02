
import threading
import time
from collections import deque
from src.sync_utils import queue_condition

temperature_averages = {}
data_queue = {}

def process_temperatures(sensor_id):
    data_queue[sensor_id] = deque(maxlen=10) 
    
    while True:
        with queue_condition:
            queue_condition.wait()
            if data_queue[sensor_id]:
                temperature_averages[sensor_id] = sum(data_queue[sensor_id]) / len(data_queue[sensor_id])

def add_to_queue(sensor_id, value):
    with queue_condition:
        data_queue[sensor_id].append(value)
        queue_condition.notify()

