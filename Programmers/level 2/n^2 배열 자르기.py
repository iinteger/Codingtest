def solution(n, left, right):
    #     matrix = []
    #     for i in range(1, n+1):
    #         temp = []
    #         for j in range(1, i):
    #             temp.append(i)
    #         for j in range(i, n+1):
    #             temp.append(j)
    #         matrix.append(temp)

    #     matrix_1d = []
    #     for row in matrix:
    #         for item in row:
    #             matrix_1d.append(item)

    #     return matrix_1d[left:right+1]

    matrix = []

    for i in range(int(left), int(right + 1)):
        j = i % n

        if i // n < j:
            item = j + 1
        else:
            item = i // n + 1
        matrix.append(item)

    return matrix

# 주석된 풀이로 풀었다가 시간초과
# 제한조건상 리스트가 굉장히 거대해질 수 있기 때문에 인덱스에 해당하는 식을 일반화함
# left, right는 정수여야 하는데 테스트케이스상 오류가 있는듯 함... 질문을 참고함