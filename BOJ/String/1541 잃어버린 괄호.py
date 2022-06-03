import sys
input = sys.stdin.readline

info = str(input().strip())
new_info = []
ans = []

info = info.split('-')
for i in info:
    i = i.split('+')
    x = 0
    for j in i:
        x += int(j)
    new_info.append(x)

ans = new_info[0]
for i in range(len(new_info)-1):
    ans -= new_info[i+1]

print(ans)
