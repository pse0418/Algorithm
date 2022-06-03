n = int(input())
data = list(map(int, str(n)))
data.sort(reverse = True)
print(''.join(map(str, data)))
