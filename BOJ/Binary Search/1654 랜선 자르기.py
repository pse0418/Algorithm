import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for i in range(k)]

right = max(lan)
left = 1

while(left <= right):
    mid = (right + left) // 2
    count = 0
    for i in lan:
        count += i // mid
    if(count >= n):
        left = mid + 1
    else:
        right = mid - 1
        
print(right)
