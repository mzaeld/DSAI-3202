import time
import multiprocessing

class ConnectionPool:
    def __init__(self, max_connections):
        """Initialize the connection pool with a semaphore."""
        self.pool = [f"Connection-{i}" for i in range(max_connections)]
        self.semaphore = multiprocessing.Semaphore(max_connections)
        self.lock = multiprocessing.Lock()  # Ensure thread-safe pool modifications

    def get_connection(self):
        """Acquire a connection from the pool."""
        self.semaphore.acquire()
        with self.lock:  # Ensure safe access
            if self.pool:
                return self.pool.pop()
        return None  # Should not happen with proper semaphore use

    def release_connection(self, connection):
        """Release a connection back to the pool."""
        with self.lock:
            self.pool.append(connection)
        self.semaphore.release()
