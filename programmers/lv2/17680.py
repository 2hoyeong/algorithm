# https://school.programmers.co.kr/learn/courses/30/lessons/17680
# 2018 KAKAO BLIND RECRUITMENT
# 캐시

def solution(cacheSize, cities):
    answer = 0
    cache = {}
    for c in cities:
        city = c.lower()
        if city in cache:
            answer += 1
            del cache[city]
            cache[city] = 1

        else:
            answer += 5
            cache[city] = 1
            if len(cache.keys()) > cacheSize:
                first = list(cache.keys())[0]
                del cache[first]
        
        
    return answer
