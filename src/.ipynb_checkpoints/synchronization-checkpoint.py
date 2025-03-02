import threading
lock = threading.RLock()
condition = threading.Condition(lock)
