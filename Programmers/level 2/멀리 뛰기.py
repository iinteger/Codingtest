def solution(n):
    answer = 0
    counts = [0] * (n + 1)
    counts[0] = 1
    counts[1] = 1

    for i in range(2, n + 1):
        counts[i] = counts[i - 1] + counts[i - 2]

    return counts[n] % 1234567

# 쉬운 문제