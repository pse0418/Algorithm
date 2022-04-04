from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:   #3 + 30 > 30 + 3
        return -1
    else:
        return 1

def solution(numbers):
    numbers = list(map(str, numbers))
    
    numbers = sorted(numbers, key=cmp_to_key(compare))
    
    if numbers[0] == "0":
        return "0"
    
    return ''.join(map(str, numbers))
