def solution(numbers, target):
    result = []
    for i in range(len(numbers)-1):
        result.append([])

    result[0] = [numbers[0]+numbers[1],
                 numbers[0]-numbers[1],
                 -numbers[0]+numbers[1],
                 -numbers[0]-numbers[1]]

    for i in range(1, len(numbers)-1):
        for j in range(len(result[i-1])):
            result[i].append(result[i-1][j]+numbers[i+1])
            result[i].append(result[i-1][j]-numbers[i+1])

    return result[-1].count(target)

# 리스트의 매 회차에 가능한 모든 경우의 수를 계산해 넣음

# 최고 득표 풀이...
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
