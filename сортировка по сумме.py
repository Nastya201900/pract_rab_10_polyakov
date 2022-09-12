def sumDigits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum
f = open('input.txt', 'r')
l = sorted(list(map(int, f.read().split())), key=sumDigits)
f.close()
f = open('output.txt', 'w')
f.write(''.join([str(x) + ' ' for x in l]))
f.close()
