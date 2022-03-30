import heapq

def solution(jobs):
    answer = 0
    time = 0
    count = 0
    heap = []
    
    jobs.sort(key=lambda x:-x[0])

    while(jobs or heap):
        while(jobs and jobs[-1][0] <= time):
            a, b = jobs.pop()
            answer -= a
            heapq.heappush(heap, b)
        if(not heap):
            time = jobs[-1][0]
            continue
        time += heapq.heappop(heap)
        answer += time
        count += 1
                
    return answer//count
