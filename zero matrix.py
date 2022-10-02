def changeRowColumn(mat, M, N, x, y):
 
    for j in range(N):
        if mat[x][j]:
            mat[x][j] = -1
 
    for i in range(M):
        if mat[i][y]:
            mat[i][y] = -1

def convert(mat):
 
    if not mat or not len(mat):
        return
 
    (M, N) = (len(mat), len(mat[0]))
 
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0: 
                changeRowColumn(mat, M, N, i, j)
 
    for i in range(M):
        for j in range(N):
            if mat[i][j] == -1:
                mat[i][j] = 0
    return mat
mat = [
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1]
    ]
mat=convert(mat)
print(mat)