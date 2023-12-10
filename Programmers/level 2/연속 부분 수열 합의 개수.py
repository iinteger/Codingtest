def solution(elements):
    sum_list = []

    # 1 ~ n-1 까지 계산
    for i in range(1, len(elements)):

        for j in range(len(elements)):
            # 부분수열이 리스트를 한바퀴 돌지 않을 때
            if j + i <= len(elements):
                sum_list.append(sum(elements[j:j + i]))

            # 부분수열이 리스트를 한바퀴 돌아서 완성될 때
            else:
                sum_list.append(sum(elements[j:]) + sum(elements[:i + j - len(elements)]))

    sum_list.append(sum(elements))

    return len(set(sum_list))