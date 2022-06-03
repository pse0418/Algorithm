import sys
input = sys.stdin.readline

n, m = map(int,input().split())
time = list(map(int,input().split()))

right = sum(time)
left = max(time)

while(left <= right):
    mid = (right + left) // 2
    length = 0
    count = 1
    for i in time:
        length += i
        if(length > mid):
            length = i
            count += 1
    if (count <= m):
        right = mid - 1
    else:
        left = mid + 1

print(left)
