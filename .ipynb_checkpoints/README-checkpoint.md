#description
This repository is for parallel and distributed computing for DSAI3202

This is Assignment 1

Part I:
Square functions:
• Time the program in these scenarios on the random list.
    o A sequential for loop.
    o A multiprocessing for loop with a process for each number.
    o A multiprocessing pool with both map() and apply().
    o A concurrent.futures ProcessPoolExecutor.
• What are your conclusions?
- The multiprocessing for loop has an error, and that is because there are too many processes for the OS to handle.
  
• Redo the test with 10^7 numbers.
• Test both synchronous and asynchronous versions in the pool.
• What are your conclusions?



Semaphores:
What happens if more processes try to access the pool than there are available
connections?
- If there are more processes than the available connections they will have to wait until a connection is released. In my case, I put max_connections as 2 whilst the number of processes are 5 so that means when the 2 processes uses the the connections then the other 3 will wait until the connection is released.

How does the semaphore prevent race conditions and ensure safe access to the
connections?
- The semaphore it organizes and prevents conflicts by acting as a controller, it uses the acquire() and release() to prevent race conditions.
- They use acquire as a requesting access, if connections available then it will gets access and if they are not available the processes will have to wait.
- They use the release() to free the connections when the processes is done with the connections.






Part II:





