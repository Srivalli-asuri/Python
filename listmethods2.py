# 1. Take two dimensional array (square matrix) print diagnol values in list
def diagonal_elements(matrix):
    diag=[]
    for i in range(len(matrix)):
        diag.append(matrix[i][i])
    print("diagonal values",diag)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal_elements(matrix)
# 2.Print anti diagonal values inist
# V= [
# [1,3,6],
# [4,7,5],
# [6,4,9]
# ]
def diagonal_elements(matrix):
    diag = []
    for i in range(len(matrix)):
        diag.append(matrix[i][len(matrix)-1-i])
    print(" Anti-Diagonal values:", diag)
matrix= [
[1,3,6],
[4,7,5],
[6,4,9]
]
diagonal_elements(matrix)
