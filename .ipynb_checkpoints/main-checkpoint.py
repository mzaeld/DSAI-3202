#!/usr/bin/env python3
import threading
import time
from src.sensor import simulate_sensor, latest_temperatures
from src.processor import process_temperatures, add_to_queue
from src.display import initialize_display, update_display

def main():
    num_sensors = 3
    sensor_threads = []
    processor_threads = []

    # Start sensor threads
    for i in range(num_sensors):
        t = threading.Thread(target=simulate_sensor, args=(i,), daemon=True)
        sensor_threads.append(t)
        t.start()

    # Start processing threads
    for i in range(num_sensors):
        t = threading.Thread(target=process_temperatures, args=(i,), daemon=True)
        processor_threads.append(t)
        t.start()

    # Start display
    initialize_display()
    display_thread = threading.Thread(target=update_display, daemon=True)
    display_thread.start()

    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")

if __name__ == "__main__":
    main()
