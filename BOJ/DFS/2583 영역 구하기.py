import sys
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
area_list = []

def dfs(x, y, m, n):
    global area
    area = 1
    to_visit = []
    to_visit.append([x, y])
    info[y][x] = 1

    while to_visit:
        x, y = to_visit.pop()
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue
            if info[next_y][next_x] != 0:
                continue
            if info[next_y][next_x] == 0:
                to_visit.append([next_x, next_y])
                info[next_y][next_x] = 1
                area += 1

count = 0
m, n, k = map(int, input().split())
info = [[0 for i in range(n)] for i in range(m)]

for _ in range(k):
    left_x, left_y, right_x, right_y = map(int, input().split())
    for y in range(left_y, right_y):
        for x in range(left_x, right_x):
            info[y][x] = 1

for y in range(m):
    for x in range(n):
        if(info[y][x] == 0):
            dfs(x, y, m, n)
            count += 1
            area_list.append(area)

area_list.sort()

print(count)
area_list = [str(a) for a in area_list]
print(" ".join(area_list))
