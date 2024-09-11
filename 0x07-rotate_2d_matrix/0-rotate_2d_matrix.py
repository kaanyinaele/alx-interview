#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix by 90 degrees clockwise in-place.
    
    Args:
        matrix (list of list): A 2D matrix, where each sublist represents a row.

    Do not return anything. The matrix is modified in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (convert rows to columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row to achieve the 90 degrees clockwise rotation
    for i in range(n):
        matrix[i].reverse()
