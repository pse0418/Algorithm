from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    data = deque()
    
    for i in range(len(progresses)):
        data.append([math.ceil((100-progresses[i]) / speeds[i])])
    
    while(data):
        count = 1
        popdata = data.popleft()
        while(data and popdata >= data[0]):
            data.popleft()
            count += 1
        answer.append(count)
    
    return answer
