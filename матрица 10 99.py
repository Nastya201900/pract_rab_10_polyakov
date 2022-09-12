import random
print('Матрица А:')
x = 4
a=[]
c=0
q=0
w=0
a=[[random.randint(10, 99) for i in range(x)] for j in range(x)]
for i in range(len(a)):
    for j in range(len(a[i])):
        print("{:4d}".format(a[i][j]), end='')
    print()
for i in range(x):
   q+=1
   for j in range(x):
       w+=1
       if a[i][j]>c:
           c=a[i][j]
print('Максимальный элемент :', 'a[',q,',',w,']=', c)
for i in range(x):
   q+=1
   for j in range(x):
       w+=1
       if a[i][j]<c:
           c=a[i][j]
print('Минимальный элемент :', 'a[',q,',',w,']=', c)