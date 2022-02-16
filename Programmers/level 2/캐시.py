def solution(cacheSize, cities):
    cache = []

    answer = 0
    for city in cities:
        city = city.lower()

        if city not in cache:
            answer += 5

            if len(cache) == cacheSize:
                cache.append(city)
                del cache[0]
            else:
                cache.append(city)

        elif city in cache:
            del cache[cache.index(city)]
            cache.append(city)
            answer += 1

    return answer

# 쉬운 문제. 캐싱된 데이터는 맨 뒷쪽으로 캐시 순서를 갱신해야 함