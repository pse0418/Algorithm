from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    data = deque([], bridge_length)
    truck_weights = deque(truck_weights)
    time = 0
    sum_weight = 0
    
    for _ in range(bridge_length):
        data.append(0)
    
    while(truck_weights):
        a = truck_weights.popleft()
        data.append(a)
        sum_weight += a
        time += 1
        sum_weight -= data.popleft()
        while(truck_weights and sum_weight+truck_weights[0] > weight):
            time += 1
            data.append(0)
            sum_weight -= data.popleft()
    
    return time+bridge_length
