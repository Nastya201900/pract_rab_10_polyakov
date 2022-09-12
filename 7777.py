import random
N = 10
a = [156, 819, 600, 587, 96, 226, 284, 26, 521, 555]
print(a)
print('Метод пузырька:')
p = 0
for i in range(N-1):
    for j in range(N-2, i-1, -1):
        if a[j + 1] < a[j]:
            p += 1
            a[j], a[j+1] = a[j+1], a[j]
print('Отсортированный массив: ')
print(a)
print('Число перестановок',p)
print('Метод выбора:')
k = 0
for i in range(N-1):
    nMin = i
    for j in range(i+1, N):
        if a[j] < a[nMin]:
            nMin = j
    if i != nMin:
        a[i], a[nMin] = a[nMin], a[i]
    k += 1
print('Отсортированный массив: ')
print(a)
print('Число перестановок',k)
print('Метод выбора :')
def QuickSort(a):
    cc = 0
    if len(a) <= 1:
        return a
    else:
        elem = a[0]
        L = list(filter(lambda x: x < elem, a))
        M = [i for i in a if i == elem]
        R = list(filter(lambda x: x > elem, a))
        cc += 1
        print(int(cc))
        return QuickSort(L) + M + QuickSort(R)
print(QuickSort(a))