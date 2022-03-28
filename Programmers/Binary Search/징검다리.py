def solution(distance, rocks, n):
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    
    left = 0
    right = distance
    
    while(left <= right):
        mid = (left + right) // 2
        bfrock = []
        bfrock.append(0)
        
        for rock in rocks:
            if (rock - bfrock[-1]) > mid:
                bfrock.append(rock)
        
        if(len(bfrock) < len(rocks) - n):
            right = mid - 1
        else:
            left = mid + 1
            
    answer = left
    
    return answer
