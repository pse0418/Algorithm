from collections import deque

def solution(priorities, location):
    answer = 0
    data = deque()
    j = 0
    
    for i in priorities:
        data.append([i, j])
        j += 1
    
    while(data):
        max_value = max(data, key=lambda item: item[0])[0]
        while(data[0][0] < max_value):
            data.append(data.popleft())
        a = data.popleft()
        answer += 1
        if(a[1] == location):
            return answer
