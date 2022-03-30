def solution(phone_book):
    dic = {}
    answer = True

    for phone in phone_book:
        dic[phone] = 1
    
    for phone in phone_book:
        for i in range(len(phone)):
            a = phone[:(i+1)]
            if a in dic:
                if a != phone:
                    answer = False

    return answer
