def solution(genres, plays):
    answer = []
    hashmap = {}
    count = {}

    for i in range(len(genres)):

        if genres[i] in hashmap:
            hashmap[genres[i]] += plays[i]
            count[genres[i]].append((i, plays[i]))
            continue

        hashmap[genres[i]] = plays[i]
        count[genres[i]] = []
        count[genres[i]].append((i, plays[i]))

    hashmap = dict(sorted(hashmap.items(), key = lambda x: x[1], reverse = True))
    
    for i in hashmap:
        count[i] = sorted(count[i], key = lambda x: x[1], reverse = True)

    for i in hashmap:
        a = 0
        for j in count[i]:
            a += 1
            if a > 2:
                continue
            answer.append(j[0])

    return answer
