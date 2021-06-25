n, m = map(int, input().split())
a, b, d = map(int, input().split())

# 0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽
# 입력을 받은 뒤, 북 서 남 동 순으로 0, 1, 2, 3으로 재배치 : 풀기 편하게 하려고


if d == 1:
    d = 3
elif d == 3:
    d = 1

moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
Map = []
for i in range(n):
    Map.append(list(input().split()))

visited = Map
visited[a][b] = "1"
count = 1


# 사방에 방문할 수 있는 곳이 있는지 체크
def check_around():
    if visited[a+1][b] == "0" or visited[a-1][b] == "0" or visited[a][b+1] == "0" or visited[a][b-1] == "0":
        return True
    else:
        return False


# 뒷방향으로 갈 수 있는지 체크
def check_visitable_backward():
    global a, b, count, d

    if Map[a-moves[d][0]][b-moves[d][1]] == "1":  # 뒤가 바다일 때
        return False
    else:  # 뒤가 육지일때
        a -= moves[d][0]
        b -= moves[d][1]


while True:
    print("location :", a, b)
    if not check_around():  # 사방이 바다이거나 방문한곳일때 -> 종료 or 뒤로가기
        d += 1
        d %= 4
        if not check_visitable_backward():  # 뒤가 바다일 때
            break

    else:  # 방문하지 않은 곳이 있을 때
        d += 1
        d %= 4  # 왼쪽으로 회전

        if visited[a+moves[d][0]][b+moves[d][1]] == "1":  # 가려는 곳이 갔던곳이나 바다일 때
            pass
        else:
            visited[a + moves[d][0]][b + moves[d][1]] = "1"
            a += moves[d][0]
            b += moves[d][1]
            count += 1

print(count)