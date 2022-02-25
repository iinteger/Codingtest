def solution(n):
    energy = 1

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            energy += 1

    return energy


# 쉬운 문제
# 그런데 베스트 답안이 창의적임
# 이진수로 변환했을 때 1이 체크된 각 자릿수는 점프로 간 최대 거리
def solution(n):
    return bin(n).count('1')