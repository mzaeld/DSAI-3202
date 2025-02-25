#description
This repository is for parallel and distributed computing for DSAI3202
this is the fourth lab, there will be part 1 and part 2

1) Which synchronization metric did you use for each of the tasks?
   - used Rlock in sensor for updates in latest_temperature
   - used queue to read and conditions in processor to synchronized the queue processing thread with sensor updates 
   - used Rlock in display to prevents inconsistent display updates
2) Why did the professor not ask you to compute metrics?
    - in here the speed does not matter as much compared to the previous labs,in here the goal is to make thread synchronization,data sharing and concurrency handling so the metrics does not really matter.
