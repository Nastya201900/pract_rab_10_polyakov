counter = 0
def tumba(n, s):
    global counter
    for c in ch:
        if n < k:
            tumba(n+1, s+c)
        else:
            w = s+c
            i = 1
            while i < n:
                if w[i-1] == w[i]: break
                i += 1
            if i < n:
                counter += 1
                print(w)
ch = ['Ы', 'Ш', 'Ч', 'О']
k = int(input())
tumba(1,'')
print(counter)