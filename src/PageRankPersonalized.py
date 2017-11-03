# Personalized PageRank - Same as RWR
# With Minor Difference - Restart Vector vs. Seeds Vector

import numpy as np

# Iteration Time for Random Walk
# Default - Iteration Time is Set to 20
ITERATION_TIME = 20
# Iteration Delta for Random Walk
# Default - Iteration Delta is Set to (1e-10) / (1 * 10 ** -10)
ITERATION_DELTA = 1e-10


# Personalized PageRank Function
# Parameters List
# @Param seeds - Seed set, List of Seeds' Position (Col Num in Transition Matrix)
# @Param trans_2d_list - Transition Matrix in the form of 2D List
# @Param alpha - Probability of Random Walk to Neighbors, Between 0 and 1
def personalized_page_rank(seeds, trans_2d_list, alpha=0.9):
    # Row Number and Col Number in Transition Matrix
    row_num = len(trans_2d_list)

    # Seed Vector (N * 1)
    # Values at Corresponding Position = 1/NumOfSeeds
    # Otherwise = 0
    seed_list = []
    for i in range(0, row_num):
        if i in seeds:
            seed_list.append([1/len(seeds)])
        else:
            seed_list.append([0])

    # PR vector (N * 1)
    # Assumption - Initial PR Vector is the Seed Vector
    # Transform to Lists to Matrix
    seed_vector = np.matrix(seed_list)
    pr_vector = np.matrix(seed_list)
    trans_matrix = np.matrix(trans_2d_list)

    # Calculate PR Vector with Formula Iteratively
    # pr_new = alpha * TransitionMatrix * pr_old + (1 - alpha) * SeedVector
    for i in range(0, ITERATION_TIME):
        pr_vector = alpha * trans_matrix * pr_vector + (1 - alpha) * seed_vector

    pr_list = pr_vector.tolist()
    # Return the Final PageRank Score Vector
    return pr_list
# ----- End of Personalized PageRank
