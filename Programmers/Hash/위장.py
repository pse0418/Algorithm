def solution(clothes):
    hashmap = {}
    answer = 1
    
    for cloth in clothes:
        if cloth[1] in hashmap:
            hashmap[cloth[1]] += 1
            continue
        hashmap[cloth[1]] = 2

    for i in hashmap.values():
        answer *= i

    return answer-1
