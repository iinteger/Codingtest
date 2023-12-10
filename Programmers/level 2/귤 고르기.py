def solution(k, tangerine):
    count = {}
    for i in tangerine:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    result = 0
    for i in count:
        k -= i[1]
        result += 1
        if k <= 0:
            return result