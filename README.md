# Fuzzy-clustering-with-EM(Expectation Maximization)-algorithm
This is the programming assignment of Data Mining course(course code:CSIT5210/MSBD5002) in CSE, HKUST 2017 Fall.
## Prerequisites
- Python3+
- Numpy
## How to run ?
`python3 fcem.py`
## Problem description
Based on the clickstream event frequency pattern in Q2Q3_input.csv for a given lecture video, apply EM algorithm to cluster the students into two classes with the following initial settings:
- Initial centers: c1 =(1,1,1,1,1,1), c2 = (0,0,0,0,0,0)
- Cluster features: frequency patterns for 6 given clickstream events: load_video,pause_video,play_video,seek_video, speed_change_video and stop_video, you can find them in Q2Q3_input.csv. You need to:
  - (a). Report the updated centers and SSE for the first two iterations.
  - (b). Report the overall iteration step when your algorithm terminates
  - (c). Report the final converged centers for each cluster.
  
Please use the terminate condition below:
- The sum of L1-distance for each pair of old-new center is smaller than 0.001, or
- The iteration step is greater than the maxinum iteration step 50.
