# Rescaling/Normalizing the Final PageRank Result
# For Output Use


# Rescaling to the range of [0, 1]
# Highest PR is rescaled to 1, Lowest PR is rescaled to 0
# Return List is an 1D List
# @Param - PageRank Result List (2D List)
def rescale_0_1(pr_result):
    # max(pr_result) and min(pr_result) will get an one-element LIST
    # Containing max/min value of PR, i.e. [maxPR] or [minPR]
    pr_max = max(pr_result)[0]
    pr_min = min(pr_result)[0]

    # If Max PR score == Min PR score, return the Original result
    if pr_max == pr_min:
        return pr_result

    # Return List
    rescaled_result = []
    # Rescale and Preserve original order
    for pr in pr_result:
        # Rescaled PR = (OriginalPR - PR_Min) / PR_Difference
        scaled_pr = (pr[0] - pr_min) / (pr_max - pr_min)
        rescaled_result.append(scaled_pr)

    return rescaled_result
# ----- End Rescale to [0, 1] -----
