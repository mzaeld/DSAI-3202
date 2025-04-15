"""
Main entry point for the maze runner game.
"""

import argparse
import multiprocessing
from src.game import run_game
from src.explorer import Explorer
from src.maze import create_maze


def run_explorer_process(maze_type, width, height, result_queue, use_a_star=False):
    maze = create_maze(width, height, maze_type)
    # --- Enhancement: Use A* Search if specified ---
    explorer = Explorer(maze, visualize=False, use_a_star=use_a_star)
    time_taken, moves = explorer.solve()
    result_queue.put({
        'time': time_taken,
        'moves': len(moves),
        'backtracks': explorer.backtrack_count
    })


def run_multiprocessing_explorers(maze_type, width, height, use_a_star, num_processes=4):
    processes = []
    result_queue = multiprocessing.Queue()

    for _ in range(num_processes):
        p = multiprocessing.Process(
            target=run_explorer_process,
            args=(maze_type, width, height, result_queue, use_a_star)  # Pass use_a_star
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = [result_queue.get() for _ in processes]

    print("\n=== Multiprocessing Explorer Summary ===")
    for idx, res in enumerate(results):
        print(f"Explorer #{idx + 1}: Time={res['time']:.2f}s | Moves={res['moves']} | Backtracks={res['backtracks']}")

    best = min(results, key=lambda x: x['moves'])
    print(f"\n🏆 Best Performer: {best['moves']} moves in {best['time']:.2f}s with {best['backtracks']} backtracks.")


def main():
    parser = argparse.ArgumentParser(description="Maze Runner Game")
    parser.add_argument("--type", choices=["random", "static"], default="random",
                        help="Type of maze to generate (random or static)")
    parser.add_argument("--width", type=int, default=30,
                        help="Width of the maze (default: 30, ignored for static mazes)")
    parser.add_argument("--height", type=int, default=30,
                        help="Height of the maze (default: 30, ignored for static mazes)")
    parser.add_argument("--auto", action="store_true",
                        help="Run automated maze exploration")
    parser.add_argument("--visualize", action="store_true",
                        help="Visualize the automated exploration in real-time")
    parser.add_argument("--multiprocessing", action="store_true",
                        help="Run multiple explorers in parallel (no visualization)")
    # --- Enhancement: CLI flag to use A* Search ---
    parser.add_argument("--a_star", action="store_true",
                        help="Use A* algorithm instead of default search")

    args = parser.parse_args()

    if args.multiprocessing:
        run_multiprocessing_explorers(args.type, args.width, args.height, args.a_star)

    elif args.auto:
        maze = create_maze(args.width, args.height, args.type)
        # --- Enhancement: Pass A* flag to Explorer ---
        explorer = Explorer(maze, visualize=args.visualize, use_a_star=args.a_star)
        time_taken, moves = explorer.solve()
        print(f"Maze solved in {time_taken:.2f} seconds")
        print(f"Number of moves: {len(moves)}")
        if args.type == "static":
            print("Note: Width and height arguments were ignored for the static maze")

    else:
        run_game(maze_type=args.type, width=args.width, height=args.height)


if __name__ == "__main__":
    main()
