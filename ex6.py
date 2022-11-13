'''Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Go to the editor
Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]'''


def two_arreys(m, n):

    l = []
    for i in range(m+1):
        for j in range(n+1):
            l.append(0)

    for i in range(m+1):
        for j in range(n+1):
            l[i][j] = i * j
            return l


two_arreys(3, 4)
