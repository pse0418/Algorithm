import sys
input = sys.stdin.readline

x, y = map(int,input().split())
z = (y * 100) // x
right = x
left = 0

while(left <= right):
    mid = (left + right) // 2
    avg = ((mid + y) * 100) // (x + mid)
    if(z >= 99):
        left = -1
        break
    if(avg > z):
        right = mid - 1
    else:
        left = mid + 1

print(left)
