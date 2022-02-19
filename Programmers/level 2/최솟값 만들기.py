def solution(A, B):
    A.sort(reverse=True)
    B.sort()

    sum = 0

    for i in range(len(A)):
        sum += A[i] * B[i]

    return sum

# 쉬운 문제