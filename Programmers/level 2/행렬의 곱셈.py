def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([0] * len(arr2[0]))

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr2)):
                sum += arr1[i][k] * arr2[k][j]
            answer[i][j] = sum

    return answer


# 루프문 정리만 잘하면 쉬운 문제
# 다른 풀이에서는 행렬을 전치해서 더 간단하게 계산함
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];
print("결과 : {}".format(productMatrix(a,b)));