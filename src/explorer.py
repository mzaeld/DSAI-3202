"""
Maze Explorer module that implements automated maze solving.
"""

import time
import heapq
import pygame
from typing import Tuple, List, Optional, Deque
from collections import deque
from .constants import BLUE, WHITE, CELL_SIZE, WINDOW_SIZE

class Explorer:
    def __init__(self, maze, visualize: bool = False, use_a_star: bool = False):
        self.maze = maze
        self.x, self.y = maze.start_pos
        self.direction = (1, 0)  # Start facing right
        self.moves = []
        self.start_time = None
        self.end_time = None
        self.visualize = visualize
        self.move_history = deque(maxlen=3)
        self.backtracking = False
        self.backtrack_path = []
        self.backtrack_count = 0
        self.use_a_star = use_a_star

        if visualize:
            pygame.init()
            self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
            pygame.display.set_caption("Maze Explorer - Automated Solving")
            self.clock = pygame.time.Clock()

    # A* Search Algorithm (Enhancement)
    def a_star_search(self) -> List[Tuple[int, int]]:
        """Solve the maze using A* search."""
        start = self.maze.start_pos
        goal = self.maze.end_pos
        open_list = []
        heapq.heappush(open_list, (0 + self.heuristic(start, goal), 0, start, []))
        closed = set()

        while open_list:
            f, g, current, path = heapq.heappop(open_list)

            if current in closed:
                continue
            closed.add(current)
            path = path + [current]

            if current == goal:
                self.moves = path
                return path

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if (0 <= neighbor[0] < self.maze.width and
                    0 <= neighbor[1] < self.maze.height and
                    self.maze.grid[neighbor[1]][neighbor[0]] == 0 and
                    neighbor not in closed):
                    heapq.heappush(open_list, (
                        g + 1 + self.heuristic(neighbor, goal),
                        g + 1,
                        neighbor,
                        path
                    ))

        return []

    # Manhattan distance heuristic for A* (Enhancement)
    def heuristic(self, current: Tuple[int, int], goal: Tuple[int, int]) -> int:
        """Manhattan distance heuristic."""
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def turn_right(self):
        x, y = self.direction
        self.direction = (-y, x)

    def turn_left(self):
        x, y = self.direction
        self.direction = (y, -x)

    def can_move_forward(self) -> bool:
        dx, dy = self.direction
        new_x, new_y = self.x + dx, self.y + dy
        return (0 <= new_x < self.maze.width and
                0 <= new_y < self.maze.height and
                self.maze.grid[new_y][new_x] == 0)

    def move_forward(self):
        dx, dy = self.direction
        self.x += dx
        self.y += dy
        current_move = (self.x, self.y)
        if not self.moves or self.moves[-1] != current_move:
            self.moves.append(current_move)
        self.move_history.append(current_move)
        if self.visualize:
            self.draw_state()

    def is_stuck(self) -> bool:
        return len(self.move_history) == 3 and all(
            self.move_history[0] == pos for pos in self.move_history
        )

    # Backtracking logic (Dead-End Pruning Enhancement)
    def backtrack(self) -> bool:
        if not self.backtrack_path:
            self.backtrack_path = self.find_backtrack_path()  # Enhanced logic for dead-end pruning
        if self.backtrack_path:
            next_pos = self.backtrack_path.pop()
            self.x, self.y = next_pos
            self.backtrack_count += 1
            if self.visualize:
                self.draw_state()
            return True
        return False

    # Finding backtrack path (Dead-End Pruning Enhancement)
    def find_backtrack_path(self) -> List[Tuple[int, int]]:
        path = []
        visited = set()
        for pos in reversed(self.moves):
            if pos in visited:
                continue
            visited.add(pos)
            path.append(pos)
            if self.count_available_choices(pos) > 1:
                return path[::-1]
        return path[::-1]

    def count_available_choices(self, pos: Tuple[int, int]) -> int:
        x, y = pos
        choices = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < self.maze.width and
                0 <= new_y < self.maze.height and
                self.maze.grid[new_y][new_x] == 0):
                choices += 1
        return choices

    def draw_state(self):
        self.screen.fill(WHITE)
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if self.maze.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0),
                                     (x * CELL_SIZE, y * CELL_SIZE,
                                      CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, (0, 255, 0),
                         (self.maze.start_pos[0] * CELL_SIZE,
                          self.maze.start_pos[1] * CELL_SIZE,
                          CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.maze.end_pos[0] * CELL_SIZE,
                          self.maze.end_pos[1] * CELL_SIZE,
                          CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, BLUE,
                         (self.x * CELL_SIZE, self.y * CELL_SIZE,
                          CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        self.clock.tick(30)

    def print_statistics(self, time_taken: float):
        print("\n=== Maze Exploration Statistics ===")
        print(f"Total time taken: {time_taken:.2f} seconds")
        print(f"Total moves made: {len(self.moves)}")
        print(f"Number of backtrack operations: {self.backtrack_count}")
        avg_fps = len(self.moves) / time_taken if time_taken > 0 else 0
        print(f"Average moves per second: {avg_fps:.2f}")
        print("==================================\n")

    # Right-hand rule solver (unchanged logic)
    def right_hand_rule_solver(self):
        visited = set()
        visited.add((self.x, self.y))
        if self.visualize:
            self.draw_state()

        while (self.x, self.y) != self.maze.end_pos:
            if self.is_stuck():
                if not self.backtrack():
                    self.turn_left()
                    self.turn_left()
                    self.move_forward()
                self.backtracking = True
            else:
                self.backtracking = False
                self.turn_right()
                if self.can_move_forward():
                    self.move_forward()
                else:
                    self.turn_left()
                    if self.can_move_forward():
                        self.move_forward()
                    else:
                        self.turn_left()
                        if self.can_move_forward():
                            self.move_forward()
                        else:
                            self.turn_left()
                            self.move_forward()

    def solve(self) -> Tuple[float, List[Tuple[int, int]]]:
        """Solve the maze using A* or right-hand rule with backtracking."""
        self.start_time = time.time()
        if self.use_a_star:
            self.a_star_search()  # A* search is invoked here (Enhancement)
        else:
            self.right_hand_rule_solver()  # Right-hand rule logic remains unchanged
        self.end_time = time.time()
        time_taken = self.end_time - self.start_time

        if self.visualize:
            pygame.time.wait(2000)
            pygame.quit()

        self.print_statistics(time_taken)
        return time_taken, self.moves
