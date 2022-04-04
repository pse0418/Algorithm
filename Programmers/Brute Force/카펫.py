def solution(brown, yellow):
    answer = []
    sum_by = brown + yellow
    
    for i in range(brown//2+1):
        if (i+1) * (brown//2-i+1) == sum_by:
            answer = [brown//2-i+1, i+1]
            break
    
    return answer
