import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    info = str(input().strip())
    while(info != ""):
        if "()" in info:
            info = info.replace("()","")
            if info == "":
                print("YES")
                break
        else:
            print("NO")
            break
