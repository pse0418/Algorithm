def solution(participant, completion):
    a = {}
    
    for i in participant:
        if a.get(i) != None:
            a[i] += 1
            continue
        a[i] = 1
    
    for i in completion:
        a[i] -= 1
    
    reverse_hash = dict(map(reversed,a.items()))
        
    answer = reverse_hash[1]
    return answer
