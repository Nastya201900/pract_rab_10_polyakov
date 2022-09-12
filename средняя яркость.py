import random
m, n = 4, 5
print('Матрица А:')
A=[[random.randint(0, 255) for i in range(n)] for j in range(m)]
for i in range(len(A)):
    for j in range(len(A[i])):
        print("{:4d}".format(A[i][j]), end = '')
    print()
M = sum([sum(i) for i in A])/(n*m)
print("Средняя яркость ",M)
print('Результат:')
B=[[[0,255][A[j][i]>M] for i in range(n)] for j in range(m)]
for i in range(len(A)):
    for j in range(len(A[i])):
        print("{:4d}".format(B[i][j]), end = '')
    print()
print()
