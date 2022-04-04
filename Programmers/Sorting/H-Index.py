def solution(citations):
    answer = 0
    citations.sort()
    left = citations[0]
    right = citations[-1]

    if right == 0:
        return right

    while(left <= right):
        mid = (left + right) // 2
        count = 0
        for citation in citations:
            if citation >= mid:
                count += 1
        if count == len(citations):
            return count
        if count < mid:
            right = mid - 1
        else:
            left = mid + 1
    return right
