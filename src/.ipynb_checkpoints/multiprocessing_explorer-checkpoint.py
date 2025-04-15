import time
import multiprocessing
from src.maze import Maze
from src.explorer import Explorer

def run_explorer(rank, result_queue):
    """
    Function for each process to run a maze solver.
    - rank: the rank of the process
    - result_queue: a queue to send the results to the main process
    """
    start_time = time.time()
    maze = Maze(width=50, height=50, type='static')
    explorer = Explorer(maze, visualize=False)
    time_taken, moves = explorer.solve()
    end_time = time.time()

    result = {
        'rank': rank,
        'time': time_taken,
        'moves': len(moves),
        'backtracks': explorer.backtrack_count
    }

    print(f"[Rank {rank}] Finished in {end_time - start_time:.2f} seconds.")
    result_queue.put(result)

def run_multiprocessing_explorers():
    """
    Function to start multiple processes to run maze explorers in parallel.
    - The results from all processes are collected in a queue and displayed by the main process.
    """
    # Number of processes you want to run (excluding the main process)
    num_processes = 4
    result_queue = multiprocessing.Queue()

    processes = []
    for rank in range(1, num_processes + 1):
        process = multiprocessing.Process(target=run_explorer, args=(rank, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # Collect and display results
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    # Print the result summary
    print("=== Multiprocessing Explorer Summary ===")
    for r in results:
        print(f"Explorer #{r['rank']}: Time={r['time']:.2f}s | Moves={r['moves']} | Backtracks={r['backtracks']}")
    best = min(results, key=lambda x: x['moves'])
    print(f"\n🏆 Best Performer: Explorer #{best['rank']} with {best['moves']} moves.")

if __name__ == "__main__":
    run_multiprocessing_explorers()
