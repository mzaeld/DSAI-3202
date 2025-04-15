# Maze Explorer Game

A simple maze exploration game built with Pygame where you can either manually navigate through a maze or watch an automated solver find its way to the exit.

## Question 1: Explain how the automated maze explorer works

### 1. The Algorithm used by the explorer
The algorithm that was used to help in navigating the maze for the explorers is the right-hand rule algorithm. So the rule for right-hand is that the explorer will always prioritize the right first. 
    For example, if there's a wall on the the right it will follow, if there's a gap on the right it will turn right. then if there is no possibility of right anymore it will attempt to go straight, if still not possible it will go left then last choice is to U-turn.


### 2. How it handles getting stuck in loops
It handles by having the 'is_stuck' method applied in explorer.py .So this method is a boolean, this checks if the explorer has been moving for the same movement for the last 3 moves.

### 3. The Backtracking strategy it employs
The purpose of this backtracking is to retreat and try other potential paths. It is used to help the explorers when navigating. Backtracking is very essential for this maze because without it the explorer might get stuck and wont be able to retreat.
How it works? The explorer marks its visits and once it reaches a dead-end. the explorer will backtrack and retrace their steps by moving backwards until they are at a point where there is a new direction they go through and this process repeats until they reached the goal.

### 4. The statistics it provides at the end of exploration
The performance metrics that are taken into considerations are the total time taken, number of moves, backtrack operations and the average moves per second
     - Time Taken: the total time taken for the explorer to finish the maze
     - Number of Moves: the total number of moves the explorer has to take to complete the maze from start to finish
     - Number of Backtrack Operations: the total number of explorers has to backtrack whilst completing the maze.
     - Average Moves Per Second: The average number of moves the explorer made per second of exploration time.
### with visualizations

    === Maze Exploration Statistics ===
    Total time taken: 9.79 seconds
    Total moves made: 292
    Number of backtrack operations: 0
    Average moves per second: 29.81
    ==================================
    Maze solved in 9.79 seconds
    Number of moves: 292

### without visualizations

    === Maze Exploration Statistics ===
    Total time taken: 0.00 seconds
    Total moves made: 353
    Number of backtrack operations: 0
    Average moves per second: 0.00
    ==================================
    Maze solved in 0.00 seconds
    Number of moves: 353

## Question 2: Summary of results which explorer performed best
For parallelizing this program, i am using multiprocessing due to the malfunction of my vm.

        === Multiprocessing Explorer Summary ===
    Explorer #1: Time=0.01s | Moves=1279 | Backtracks=0
    Explorer #2: Time=0.00s | Moves=1279 | Backtracks=0
    Explorer #3: Time=0.01s | Moves=1279 | Backtracks=0
    Explorer #4: Time=0.01s | Moves=1279 | Backtracks=0


## Question 3: Analysis of the different maze explorers on the static maze.

In this multiprocessing, we have 4 explorers that are ran simultaneously. and based on the the number of moves they are all the same but if you looked at the time 3 of them has  time of 0.01s whilst explorer#2 has 0.00s that means explorer#2 is the best one out of all. The reason time can be small in here is because its a small maze if the maze was bigger there would be a bigger difference in the time but as of for now the number of moves matters more.

It can be seen that the number of moves is the same, The reason can be because they are all using the same algorithm (right-hand rule), and this can also because they are using the same maze so they are going through the same obstacles and path; because of this the maze becomes deterministic and there is no randomness in it.

For the backtracking, the number stays zero for all explorers this can suggest that the maze is simple enough and the algorithm is robust enough to avoid the need for backtracking. For this case using right-hand rule is not a problem but this might be difficult for more complex maze.

## Question 4: Propose and implement enhancements

### Limitations:
- since right-hand rule is a brute-force strategy, it does not consider the goal's location
- it tries every route which is a waste of moves
- it does not remember where it has been efficiently, so it may revisit the explored paths unnecessarily
- it does not work well with complex maze because as maze size increases the ineffiency becomes more prominent

### Enhancements:
Implements that I decided to use is to integrate A* search algorithm to find the optimal path (aka shortest path). The second thing I decided to implement is te dead-end pruning with backtrack optimization.

A* search algorithm: this replaces the right-hand rule algorithm. It uses priority queue to explore the most promising paths first based on estimated cost. The enhancements are made in the "explorer.py > a_star_search()"

Dead-End Pruning: This one changes the idea instead of U-turning randomly, the explorer actually remember paths and only backtracks to intersections with multiple unexplored branches.

### after enhancements
        === Multiprocessing Explorer Summary ===
    Explorer #1: Time=0.00s | Moves=128 | Backtracks=0
    Explorer #2: Time=0.00s | Moves=128 | Backtracks=0
    Explorer #3: Time=0.00s | Moves=128 | Backtracks=0
    Explorer #4: Time=0.00s | Moves=128 | Backtracks=0

## Question 5: Comparison for before and after enhancements


Performance Comparison:

Metric           | Before Enhancement    | After Enhancement
-----------------|------------------------|------------------------
Time Taken       | ~0.01s (varied)        | 0.00s (consistent)
Moves Made       | 1279 moves             | 128 moves
Backtracks       | 0                      | 0


## Trade-Offs and New Limitations

| Aspect                  | Trade-off / Limitation |
|-------------------------|------------------------|
| **Complexity**           | A* is more complex to implement than right-hand rule. |
| **Memory Usage**         | A* uses more memory to store open and closed nodes.    |
| **Adaptability**         | A* is designed for shortest path; may not adapt well to dynamic/unknown mazes like the rule-based approach. |
| **Debugging**            | Logic in dead-end pruning adds more complexity to backtrack decisions. |

---


Based on the result that we have obtained, there is a drastic change in number of moves before and after enhancements, from 1279 to 128 only. So there is less number of moves it is also faster.


 