import sys
input = sys.stdin.readline

house = []

N, C = map(int, input().split())
for _ in range(N):
    house.append(int(input()))

house.sort()

left = 1
right = house[-1]

while(left <= right):
    mid = (left + right) // 2
    router = []
    router.append(house[0])
    for i in house:
        if i - router[-1] > mid:
            router.append(i)
    if(len(router) < C):
        right = mid - 1
    else:
        left = mid + 1

print(left)
