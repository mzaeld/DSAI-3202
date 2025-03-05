from queue import Queue
from threading import RLock, Condition

# Shared data structures
latest_temperatures = {}
temperature_averages = {}

# Thread-safe queue for temperature readings
queue = Queue()

# Locks for synchronization
lock = RLock()
condition = Condition(lock)
