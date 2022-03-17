import sys
import copy
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(x, y, n, i):
    to_visit = []
    to_visit.append([x, y])

    while to_visit:
        x, y = to_visit.pop()
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                continue
            if check[next_y][next_x] <= i:
                continue
            to_visit.append([next_x, next_y])
            check[next_y][next_x] = 0

h = []
count_list = []
count = 0

n = int(input())

for _ in range(n):
    h.append(list(map(int, input().split())))

for i in range(max(map(max, h))):
    count = 0
    check = copy.deepcopy(h)
    for y in range(n):
        for x in range(n):
            if(check[y][x] > i):
                dfs(x, y, n, i)
                count += 1
    count_list.append(count)

print(max(count_list))
