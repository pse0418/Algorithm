from itertools import permutations

def solution(numbers):
    answer = 0
    num_list = []
    
    numbers = list(map(str, str(numbers)))
    
    for i in range(len(numbers)):
        a = list(map(''.join, permutations(numbers , i+1)))
        num_list.append(a)
    num_list = sum(num_list, [])    #일차원 리스트
    num_list = list(map(int, num_list)) #문자를 숫자로
    num_list = list(set(num_list))  #중복 제거
 
    # for i in num_list:
    #     count = 0
    #     for j in range(i):
    #         if i % (j+1) == 0:
    #             count +=1
    #         if count > 2:
    #             break
    #     if count == 2:
    #         print(i)
    #         answer += 1
    
    for i in num_list:
        n = 1
        if i < 2:
            continue
        while(n**2 <= i):
            n += 1
        check = False
        for j in range(2, n):
            if i % j == 0:
                check = True
                break
        if check == False:
            answer += 1
            
    return answer
