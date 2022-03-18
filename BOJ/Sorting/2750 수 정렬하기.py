n = int(input())
data = [int(input()) for i in range(n)]
data.sort(reverse = True)
while(data):
    print(data.pop())
