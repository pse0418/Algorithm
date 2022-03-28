def solution(n, times):
    times.sort()
    left = 1
    right = times[-1] * n
    print(right)
    while(left <= right):
        mid = (left + right) // 2
        total = 0
        for i in times:
            total += mid // i
        if(total >= n):
            right = mid - 1
        else:
            left = mid + 1
    answer = left
    return answer
