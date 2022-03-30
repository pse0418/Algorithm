import sys
input = sys.stdin.readline

budget = []

N = int(input())
budget = list(map(int,input().split()))
M = int(input())

budget.sort()

left = 0
right = budget[-1]

while(left <= right):
    mid = (left + right) // 2
    money = 0
    for i in budget:
        if i > mid:
            money += mid
        else:
            money += i
    if money > M:
        right = mid - 1
    else:
        left = mid + 1
    
print(right)
