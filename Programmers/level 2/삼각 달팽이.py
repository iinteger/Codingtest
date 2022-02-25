def solution(n):
    triangle = []
    for i in range(n):
        triangle.append([0] * (i + 1))

    x = 0
    y = 0
    direction = "down"  # 채워나갈 방향

    for i in range(1, int(n * (n + 1) / 2) + 1):
        triangle[y][x] = i

        if direction == "down":
            if y < n - 1 and triangle[y + 1][x] == 0:
                y += 1
            else:
                direction = "right"
                x += 1

        elif direction == "right":
            if x < n - 1 and triangle[y][x + 1] == 0:
                x += 1
            else:
                direction = "up"
                x -= 1
                y -= 1

        elif direction == "up":
            if y > 0 and triangle[y - 1][x - 1] == 0:
                y -= 1
                x -= 1
            else:
                direction = "down"
                y += 1

    answer = []
    for row in triangle:
        for item in row:
            answer.append(item)

    return answer

# direction 변수를 사용해서 지정된 방향으로 채워넣어가는 코드