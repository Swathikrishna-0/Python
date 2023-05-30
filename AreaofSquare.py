# Question: Area of Square
# Given an MxN matrix filled with X's and O's, find the largest square containing only X's and return its area.
# If there are no Xs in the entire matrix print 0.

# Approach
# To solve this problem, we will follow these steps:

# Read the matrix from the input.
# Check if a sub-matrix contains 'O'.
# Get the maximum sub-matrix area for each 'X' in the matrix.
# Get the maximum area of square containing only 'X's.
# Implement the main function to execute the above steps.
# Step-by-Step Explanation
# Step 1: Read the matrix

# First, we need to read the matrix from the input. We will create a function read_matrix(rows) that takes the number of rows as an argument and reads the matrix elements row by row.

# PYTHON
# Step 2: Check if sub-matrix contains 'O'

# Next, we will create a function check_if_sub_matrix_contains_zero(matrix, i, j, k, l) that checks if a sub-matrix contains 'O'. This function takes the matrix, the starting row and column (i, j), and the dimensions of the sub-matrix (k, l) as arguments.

# PYTHON
# Step 3: Get the maximum sub-matrix area

# Now, we will create a function get_max_sub_matrix_area(matrix, rows, columns, i, j) that finds the maximum sub-matrix area for each 'X' in the matrix. This function takes the matrix, the number of rows and columns, and the starting row and column (i, j) as arguments.

# PYTHON
# Step 4: Get the maximum area of square

# Next, we will create a function get_max_area_of_square(matrix, rows, columns) that finds the maximum area of square containing only 'X's. This function takes the matrix, the number of rows, and the number of columns as arguments.

# PYTHON
# Step 5: Main function

# Finally, we will implement the main function to execute the above steps. The main function reads the number of rows and columns, reads the matrix, and finds the maximum area of square containing only 'X's.

# PYTHON
# Now, you have a complete solution to find the largest square containing only 'X's in a given matrix.

# 4 5
# X O X O O
# X O X X X
# X X O X X
# X O O X O -> o/p => 4

# 3 3 
# O X X
# O X X 
# O O O  -> o/p => 4 


def square_area(matrix, l_x, l_y, side_length):
     count = 0 
     for i in range(l_x,l_x+ side_length):
         for j in range(l_y,l_y+side_length):
             if matrix[i][j] == 1:
                 count += 1 
             else:
                 return 0 
     return count 
m,n = map(int,input().split())
markers = {'X':1,"O":0}
matrix = [[markers[i] for i in input().split()] for _ in range(m)]
areas = []

for l_x in range(m):
    for l_y in range(n):
        for side_length in range(1, min(n- l_y+1 , m- l_x+1)):
            areas.append(square_area(matrix, l_x, l_y, side_length))
print(max(areas))

