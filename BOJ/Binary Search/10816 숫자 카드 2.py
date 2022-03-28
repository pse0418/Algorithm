import sys
input = sys.stdin.readline

arr = {}

n = int(input())
cardlist = list(map(int,input().split()))

for i in cardlist:
    if(arr.get(i)):
        arr[i] += 1
    else:
        arr[i] = 1

m = int(input())
check = list(map(int,input().split()))

for i in check:
    if(arr.get(i)):
        print(arr[i])
    else:
        print(0)
