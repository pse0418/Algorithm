def solution(answers):
    answer = []
    count = [0, 0, 0]
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == A[i % len(A)]:
            count[0] += 1
        if answers[i] == B[i % len(B)]:
            count[1] += 1
        if answers[i] == C[i % len(C)]:
            count[2] += 1
    
    for i in range(len(count)):
        if count[i] == max(count):
            answer.append(i+1)
    
    return answer
