# myPageRank
Different versions of PageRank implementations in Python

## Python Files/Functions Description
### MatrixGenerator.py
Contains functions to generate Transition Matrix
Function 1 - Generate Transition Matrix based on vertice' Out-degree

### PageRankRWR.py
Implementation of Random Walk with Restart (RWR)
Default Iterations == 20
Default Stop Iteration Delta for PR Vector == 1e-10

### PageRankPersonalized.py
Slightly different implementation of RWR
Default Iterations == 20
Default Stop Iteration Delta for PR Vector == 1e-10

### ResultRescaler.py
Contains functions to rescale/normalize original PageRank result
Function 1 - Rescale the result to the range of 0 to 1
