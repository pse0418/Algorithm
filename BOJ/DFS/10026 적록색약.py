import sys
import copy
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
color_1 = ['R', 'B', 'G']
color_2 = ['r', 'b']
info = []

def dfs(x, y, n, c):
    to_visit = []
    visited = [[0 for i in range(n)] for i in range(n)]
    to_visit.append([x, y])

    while to_visit:
        x, y = to_visit.pop()
        info[y][x] = info[y][x].swapcase()
        if info[y][x] == 'g':
            info[y][x] = 'r'
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                continue
            if info[next_y][next_x] != c:
                continue
            if visited[next_y][next_x] == 0:
                to_visit.append([next_x, next_y])
                visited[next_y][next_x] = 1


n = int(input())
count = 0
count_rg = 0

for _ in range(n):
    info.append(list(input()[:-1]))

for c in color_1:
    for y in range(n):
        for x in range(n):
            if(info[y][x] == c):
                dfs(x, y, n, c)
                count += 1

for c in color_2:
    for y in range(n):
        for x in range(n):
            if(info[y][x] == c):
                dfs(x, y, n, c)
                count_rg += 1

print(count, count_rg)
