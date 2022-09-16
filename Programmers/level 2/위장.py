def solution(clothes):
    answer = 1

    clothes_dict = {}
    for item in clothes:
        if item[1] not in clothes_dict:
            clothes_dict[item[1]] = 1
        else:
            clothes_dict[item[1]] += 1

    for i in clothes_dict:
        answer *= clothes_dict[i] + 1

    return answer - 1


# 잘못된 풀이 : 상의만 입는 경우 + 하의만 입는 경우 + 상의와 하의를 같이 입는 경우 -> 종류가 많아질 경우 계산시간이 기하급수적으로 증가함
# 올바른 풀이 : (상의만 입는 경우 + 입지 않는 경우) * (하의만 입는 경우 + 입지 않는 경우) - 1(모두 입지 않는 경우)

# 테스트케이스 1번은 옷이 1벌씩 30종류가 있는 경우인데 조합으로 접근하면 시간초과 에러가 남
# 올바른 풀이로 접근하면 시간초과 해결
