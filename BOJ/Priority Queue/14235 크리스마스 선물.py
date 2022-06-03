import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    a = list(map(int,input().split()))
    if a == [0]:
        if len(heap) == 0:
            print(-1)
        else:
            print(heapq.heappop(heap)[1])
    else:
        a.pop(0)
        for i in a:
            heapq.heappush(heap, (-i, i))
