# PageRank - Random Walk with Restart

import numpy as np

# Iteration Time for Random Walk
# Default - Iteration Time is Set to 20
ITERATION_TIME = 20
# Iteration Delta for RWR
# Default - Iteration Delta is Set to (1e-10) / (1 * 10 ** -10)
ITERATION_DELTA = 1e-10


# RWR PageRank Function
# Parameters List
# @Param seeds - Seed set, List of Seeds' Position (Col Num in Transition Matrix, start from 0)
# @Param trans_2d_list - Transition Matrix in the form of 2D List
# @Param alpha - Probability of Random Walk to Neighbors, Between 0 and 1
def rwr_page_rank(seeds, trans_2d_list, alpha=0.9):
    # Row Number and Col Number in Transition Matrix
    row_num = len(trans_2d_list)

    # RWR PR Result, N * 1 Matrix, Initialized with ALL 0
    pr_result = []
    for i in range(0, row_num):
        pr_result.append([0.0])
    pr_result_vector = np.matrix(pr_result)

    # RWR for Each Seed
    for s in seeds:
        # Restart Vector For Each Seed(N * 1)
        # Values at Corresponding Position = 1/NumOfSeeds
        # Otherwise = 0
        restart_list = []
        for i in range(0, row_num):
            if i == s:
                restart_list.append([1])
            else:
                restart_list.append([0])

        # PR vector (N * 1)
        # Assumption - Initial PR Vector is the Restart Vector
        # Transform to Lists to Matrix
        restart_vector = np.matrix(restart_list)
        pr_vector = np.matrix(restart_list)
        trans_matrix = np.matrix(trans_2d_list)

        # Calculate the PR Vector with Formula Iteratively
        # pr_new = alpha * TransitionMatrix * pr_old + (1 - alpha) * SeedVector
        for i in range(0, ITERATION_TIME):
            pr_vector = alpha * trans_matrix * pr_vector + (1 - alpha) * restart_vector

        # Sum PR Vector for Each Seed
        pr_result_vector += pr_vector
    # RWR End

    pr_result = pr_result_vector.tolist()
    # Return the Final PageRank Score Vector
    return pr_result
# ----- End of Random Walk with Restart PageRank -----
