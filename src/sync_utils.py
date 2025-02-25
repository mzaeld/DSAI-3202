#!/usr/bin/env python3
import threading

lock = threading.RLock()
queue_condition = threading.Condition()

