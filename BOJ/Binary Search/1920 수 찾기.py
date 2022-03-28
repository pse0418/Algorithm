n = int(input())
arr = {}
tmp = list(map(int,input().split()))
for i in tmp:
    arr[i] = 1
count = int(input())
tmp = list(map(int,input().split()))
for i in tmp:
    if(arr.get(i)):
        print(1)
    else:
        print(0)
