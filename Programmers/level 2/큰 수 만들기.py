def solution(number, k):
    start_index = 0
    for i in range(k):
        for j in range(start_index, len(number) - 1):
            if number[j] < number[j + 1]:
                if j == 0:
                    number = number[1:]
                    start_index = 0
                else:
                    number = number[:j] + number[j + 1:]
                    start_index = j - 1

                break
        else:
            number = number[:-1]
            start_index = len(number)

    return number

# i번째 자리보다 i+1번째 자리가 더 큰 숫자라면 i번째 자리를 삭제
# 매 루프마다 위 비교식을 0번째부터 시작했더니 10번 케이스에서 시간초과 발생
# 새 루프의 시작점을 이전 삭제 인덱스-1 번째부터 시작하는것으로 해결
# 이전 삭제 인덱스의 -2번째까지는 이전 비교를 통해 무결한 상태이기 때문