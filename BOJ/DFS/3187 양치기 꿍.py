import sys
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(x, y, r, c):
    to_visit = []
    to_visit.append([x, y])
    visited[y][x] = 1

    v = 0
    k = 0

    if info[y][x] == 'v':
        v += 1
    if info[y][x] == 'k':
        k += 1

    while to_visit:
        x, y = to_visit.pop()
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_x == c or next_y < 0 or next_y == r:
                continue
            if info[next_y][next_x] == '#':
                continue
            if visited[next_y][next_x] == 0:
                to_visit.append([next_x, next_y])
                visited[next_y][next_x] = 1
                if info[next_y][next_x] == 'v':
                    v += 1
                if info[next_y][next_x] == 'k':
                    k += 1
    return v, k


r, c = map(int, input().split())
info = [list(input().strip()) for _ in range(r)]    #리스트 붙어있는 경우

visited = [[0 for i in range(c)] for i in range(r)]

sheep = 0
wolf = 0

for y in range(r):
    for x in range(c):
        if(info[y][x] != '#' and visited[y][x] == 0):
            v, k = dfs(x, y, r, c)
            if k > v:
                sheep += k
            else:
                wolf += v

print(sheep, wolf)import sys
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(x, y, r, c):
    to_visit = []
    to_visit.append([x, y])
    visited[y][x] = 1

    v = 0
    k = 0

    if info[y][x] == 'v':
        v += 1
    if info[y][x] == 'k':
        k += 1

    while to_visit:
        x, y = to_visit.pop()
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_x == c or next_y < 0 or next_y == r:
                continue
            if info[next_y][next_x] == '#':
                continue
            if visited[next_y][next_x] == 0:
                to_visit.append([next_x, next_y])
                visited[next_y][next_x] = 1
                if info[next_y][next_x] == 'v':
                    v += 1
                if info[next_y][next_x] == 'k':
                    k += 1
    return v, k


r, c = map(int, input().split())
info = [list(input().strip()) for _ in range(r)]    #리스트 붙어있는 경우

visited = [[0 for i in range(c)] for i in range(r)]

sheep = 0
wolf = 0

for y in range(r):
    for x in range(c):
        if(info[y][x] != '#' and visited[y][x] == 0):
            v, k = dfs(x, y, r, c)
            if k > v:
                sheep += k
            else:
                wolf += v

print(sheep, wolf)
