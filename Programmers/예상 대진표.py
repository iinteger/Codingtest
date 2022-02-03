def solution(n, a, b):
    answer = 0

    if a > b:
        a, b = b, a

    answer = 1
    while True:
        if b - a == 1 and b % 2 == 0:
            break

        if a % 2 == 1:
            a += 1
        if b % 2 == 1:
            b += 1

        a /= 2
        b /= 2
        answer += 1

    return answer


# 아래는 최다 득표 풀이.

def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()