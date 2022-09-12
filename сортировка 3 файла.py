with open('mass1.txt', 'rt') as file:
    numbers = list(map(lambda n: int(n), file.read().split()))

with open('mass2.txt', 'rt') as file:
    numbers += list(map(lambda n: int(n), file.read().split()))

print(*sorted(numbers), file=open('mass3.txt', 'wt'))