import time
import random

def access_database(pool, process_id):
    """Simulates a process performing a database operation."""
    print(f"Process {process_id} is waiting for a connection...")
    
    connection = pool.get_connection()
    
    if connection:
        print(f"Process {process_id} acquired {connection}.")
        time.sleep(random.uniform(1, 3))  # Simulating work (1-3 seconds)
        print(f"Process {process_id} released {connection}.")
        pool.release_connection(connection)
        
