import sys
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(x, y, n, m):
    to_visit = []
    to_visit.append([x, y])
    visited[y][x] = 1
    size = 1

    while to_visit:
        x, y = to_visit.pop()
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_x == m or next_y < 0 or next_y == n:
                continue
            if data[next_y][next_x] == 0:
                continue
            if visited[next_y][next_x] == 0:
                to_visit.append([next_x, next_y])
                visited[next_y][next_x] = 1
                size += 1

    return size

n, m, k = map(int,input().split())
data = [[0 for _ in range(m)] for _ in range(n)]
size_data = []

for _ in range(k):
    r, c = map(int,input().split())
    data[r-1][c-1] = 1

visited = [[0 for i in range(m)] for i in range(n)]
for y in range(n):
    for x in range(m):
        if(data[y][x] == 1 and visited[y][x] == 0):
            size_data.append(dfs(x, y, n, m))

print(max(size_data))
