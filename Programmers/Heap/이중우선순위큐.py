import heapq

def solution(operations):
    answer = []
    new_operations = []
    heap = []
    heap_max = []
    count = 0
    hashmap = {}
    
    for i in operations:
        a, b = i.split()
        new_operations.append([a, int(b)])
    
    for i in new_operations:
        if i[0] == 'I':
            heapq.heappush(heap, i[1])
            heapq.heappush(heap_max, -i[1])
            if hashmap.get(i[1]) != None:
                hashmap[i[1]] += 1
            else: hashmap[i[1]] = 1
            count += 1
        if heap_max and i[0] == 'D' and i[1] == 1:
            maxpop = heapq.heappop(heap_max)
            while(hashmap[-maxpop] < 1 and heap_max):
                maxpop = heapq.heappop(heap_max)
            count -= 1
            hashmap[-maxpop] -= 1
        if heap and i[0] == 'D' and i[1] == -1:
            minpop = heapq.heappop(heap)
            while(hashmap[minpop] < 1 and heap):
                minpop = heapq.heappop(heap)
            count -= 1
            hashmap[minpop] -= 1
    
    if count >= 2:
        maxpop = heapq.heappop(heap_max)
        while(hashmap[-maxpop] < 1 and heap_max):
            maxpop = heapq.heappop(heap_max)
        hashmap[-maxpop] -= 1
        
        minpop = heapq.heappop(heap)
        while(hashmap[minpop] < 1 and heap):
            minpop = heapq.heappop(heap)
        hashmap[minpop] -= 1
        
        answer = [-maxpop, minpop]

    elif count == 1:
        a = heapq.heappop(heap)
        answer = [a, a]
        
    else:
        answer = [0, 0]
        
    return answer
