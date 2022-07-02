def solution(board):
    for y in range(len(board) - 2, -1, -1):
        for x in range(len(board[0]) - 2, -1, -1):
            if board[y][x] == 1:
                board[y][x] = min(board[y + 1][x + 1], board[y][x + 1], board[y + 1][x]) + 1

    max_value = 0
    for y in range(len(board)):
        if max(board[y]) > max_value:
            max_value = max(board[y])

    return max_value * max_value


print(solution(	[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))


# 브루트 포스 풀이 : 정확성은 모두 맞았으나 효율성에서 모두 탈락. 질문을 보고 DP 문제인것을 확인하고 풂