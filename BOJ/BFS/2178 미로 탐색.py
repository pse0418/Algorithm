import sys
from collections import deque
input = sys.stdin.readline

miro = []
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, m = map(int, input().split())

miro = [list(map(int, input()[:-1])) for _ in range(n)]

def bfs(n, m):
    to_visit = deque()
    visited = [[0 for i in range(m)] for i in range(n)]
    to_visit.append([0, 0])
    visited[0][0] = 1

    while to_visit:
        x, y = to_visit.popleft()
        if x == m - 1 and y == n - 1:
            return visited[y][x]
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            if miro[next_y][next_x] == 0:
                continue
            if visited[next_y][next_x] == 0:
                to_visit.append([next_x, next_y])
                visited[next_y][next_x] = visited[y][x] + 1
                
print(bfs(n, m))
