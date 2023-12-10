def solution(want, number, discount):
    answer = 0

    want_dict = {want[i]: number[i] for i in range(len(want))}

    i = 0
    while i + 10 <= len(discount):
        want_dict_copy = want_dict.copy()
        buy_all = True

        for j in range(10):
            if discount[i + j] in want_dict_copy:
                want_dict_copy[discount[i + j]] -= 1

        # 물품을 다 샀는지 체크
        for item in want_dict_copy.items():
            # 물품 개수가 맞지 않은 경우
            if item[1] != 0:
                buy_all = False
                break

        if buy_all:
            answer += 1

        i += 1
    return answer