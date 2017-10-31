# Transition Matrix Generator
# 1. Transition Matrix representing the Out-Degree of each vertex
#    Each column represents each vertex's outgoing edges and its value 1/N,
#    Where N is the number of Outgoing Edges of this vertex


# @Param - "Adjacency" Matrix (Symmetric, Square)
# Return - Transition Matrix in the form of 2D List
def transition_matrix_out_degree(input_matrix):
    # Get the row number and column number
    row_num = len(input_matrix)

    # Input Matrix is Empty
    if row_num == 0:
        return None

    col_num = len(input_matrix[0])

    # Transition Matrix
    result_matrix = []

    # Create Transition Matrix based on Input Matrix
    # Traverse each Row of Input Matrix Twice
    # O(RowNum * ColNum) = O(N^2)
    for r in range(0, row_num):
        # Count Non-zero value in each Row
        # Used to Calculate values in Transition Matrix
        counter = 0
        # Value List for each Row
        row_list = []

        # Count the num of Non-zero values in each Row
        for c in range(0, col_num):
            # Diagonal values should not be counted
            if input_matrix[r][c] != 0 and r != c:
                counter += 1

        # Form Transition Matrix Row by Row
        for c in range(0, col_num):
            # Diagonal values in Transition Matrix are all zero
            if input_matrix[r][c] != 0 and r != c:
                row_list.append(1/counter)
            else:
                row_list.append(0)

        # Append each row
        result_matrix.append(row_list)
    # --- End of Out-Most Loop ---

    # Transpose the Matrix (Make Columns to represent the Transition Info)
    result_matrix = [list(i) for i in zip(*result_matrix)]

    # Return Transition Matrix
    return result_matrix
# ----- End of Transition Matrix Generation -----
