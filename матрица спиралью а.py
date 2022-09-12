a, b = map(int, input().split())
spisok_matrix = [[0] * a for _ in range(b)]
dx, dy, x, y = 0, 1, 0, 0

for i in range(1, a * b + 1):
    spisok_matrix[x][y] = i
    if spisok_matrix[(x + dx) % a][(y + dy) % b]:
        dx, dy = dy, -dx
    x += dx
    y += dy
for line in spisok_matrix:
    print(*(f'{i:<3}' for i in line), sep='')