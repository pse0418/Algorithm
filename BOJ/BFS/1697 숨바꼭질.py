from collections import deque
import sys
sys.setrecursionlimit(100000)
n, k = map(int, input().split())

def bfs(n, k):
    to_visit = deque()
    visited = []
    visited = [0 for i in range(100001)]
    to_visit.append([n, 0])
    now_count = 0
    while to_visit:
        now, now_count = to_visit.popleft()
        if now-1 >= 0 and visited[now-1] == 0:
            to_visit.append([now-1, now_count+1])
            visited[now-1] = 1
        if now*2 < 100001 and visited[now*2] == 0:
            to_visit.append([now*2, now_count+1])
            visited[now*2] = 1
        if now+1 < 100001 and visited[now+1] == 0:
            to_visit.append([now+1, now_count+1])
            visited[now+1] = 1
        if now == k:
            print(now_count)
            return

bfs(n, k)
