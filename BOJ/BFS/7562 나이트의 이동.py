from collections import deque
import sys
sys.setrecursionlimit(100000)

directions = [(-2, 1), (2, 1), (-2, -1), (2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

def bfs():
    to_visit = deque()
    visited[starty][startx] = 0
    to_visit.append([startx, starty])
    while to_visit:
        x, y = to_visit.popleft()
        if x == endx and y == endy:
            return visited[y][x]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= i or ny < 0 or ny >= i:
                continue
            if visited[ny][nx] == -1:
                to_visit.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1

for _ in range(int(input())):
    i = int(input())
    startx, starty = map(int, input().split())
    endx, endy = map(int, input().split())
    visited = [[-1] * int(i) for _ in range(i)]
    print(bfs())
