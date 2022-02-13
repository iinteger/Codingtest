import itertools


def solution(k, dungeons):
    all_case = list(itertools.permutations(dungeons, len(dungeons)))

    max_count = 0
    for i in range(len(all_case)):
        rest_k = k
        count = 0
        for j in all_case[i]:
            if rest_k >= j[0]:
                rest_k -= j[1]
                count += 1
        if count > max_count:
            max_count = count

    return max_count

# itertools을 공부하는 기회가 되었음