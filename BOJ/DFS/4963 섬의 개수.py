import sys
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(x, y, w, h):
    to_visit = []
    visited = [[0 for i in range(w)] for i in range(h)]
    to_visit.append([x, y])

    while to_visit:
        x, y = to_visit.pop()
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_x >= w or next_y < 0 or next_y >= h:
                continue
            if island[next_y][next_x] == 0:
                continue
            if visited[next_y][next_x] == 0:
                to_visit.append([next_x, next_y])
                visited[next_y][next_x] = 1
                island[next_y][next_x] = 0

while True:
    island = []
    count = 0

    w, h = map(int, input().split())
    
    for _ in range(h):
        island.append(list(map(int, input().split())))
    if w == 0 and h == 0:
        break

    for y in range(h):
        for x in range(w):
            if(island[y][x] == 1):
                dfs(x, y, w, h)
                count += 1
    print(count)
