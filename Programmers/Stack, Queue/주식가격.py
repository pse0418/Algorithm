from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while(prices):
        count = 0
        price = prices.popleft()
        for i in prices:
            count += 1
            if price > i:
                break
        answer.append(count)
            
    return answer
