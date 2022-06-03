import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
buy = 0

dasom = int(input())
for _ in range(n-1):
    a = int(input())
    if a < dasom:
        continue
    heapq.heappush(heap, (-a, a))

if len(heap) == 0:
    print(0)

else:    
    first = heapq.heappop(heap)[1]
    while(dasom <= first):
        heapq.heappush(heap, (-(first-1), first-1))
        buy += 1
        dasom += 1
        first = heapq.heappop(heap)[1]
    print(buy)
