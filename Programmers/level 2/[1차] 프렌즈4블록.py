def check(board):
    checked = 0

    # 체크 여부를 표시하는 더미 보드
    # 원본 보드에 체크를 표시하면 블록의 중복이 체크되지 않음
    # check_board = board.copy()
    # 이상하게 깊은 복사가 되어 원본 배열을 오염시킴

    # 좌표 리스트로 대체
    check_location = []

    # 전체 보드를 체크하며 해당되는 부분을 0으로 변경
    for i in range(len(board) - 1):
        for j in range(len(board[0]) - 1):
            if board[i][j] != -1:
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    check_location.append((i, j))
                    check_location.append((i + 1, j))
                    check_location.append((i, j + 1))
                    check_location.append((i + 1, j + 1))

    check_location = set(check_location)
    check_location = sorted(check_location, reverse=True, key=lambda x: x[1])

    # 행렬의 뒤에서 앞으로 체크하며 삭제
    for location in check_location:
        del board[location[0]][location[1]]
        board[location[0]].append(-1)
        checked += 1

    return board, checked


def solution(m, n, board):
    board_split = []
    for row in board:
        board_split.append([i for i in row])  # 단어별로 분리

    # 계산의 용이를 위해 아랫쪽이 왼쪽으로 오도록 행렬 회전
    board_turned = []
    for i in range(len(board[0])):
        board_turned.append([board[len(board) - j - 1][i] for j in range(len(board))])

    total_checked = 0
    while True:
        board_turned, checked = check(board_turned)
        print(checked)
        if checked == 0:
            return total_checked

        total_checked += checked


# 블럭을 터뜨리고 아랫쪽으로 미는 대신, 아랫면을 왼쪽으로 오도록 회전하여 리스트를 삭제하여 자동으로 왼쪽으로 오도록 만듦