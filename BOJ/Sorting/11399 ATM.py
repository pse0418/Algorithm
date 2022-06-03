n = int(input())
data = list(map(int, input().split()))
data.sort(reverse = True)
i = 1
sum = 0
answer = 0
while(data):
    x = data.pop()
    sum = x + sum
    answer += sum
    i += 1
print(answer)
