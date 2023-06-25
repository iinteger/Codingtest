# r2 원 내에서 y축을 제외하고 1사분면 위에 존재하는 점을 구한 뒤 동일하게 r1의 점 개수를 구해서 뺌
def solution(r1, r2):
    answer = 0

    # y축을 제외하고 1사분면에서 r2 원 안에 있는 점의 갯수
    for x in range(1, r2):
        y2 = (r2 ** 2 - x ** 2) ** (1 / 2)
        answer += int(y2) + 1
    answer += 1

    # y축을 제외하고 1사분면에서 r1 원 안에 있는 점의 갯수
    for x in range(1, r1):
        y1 = (r1 ** 2 - x ** 2) ** (1 / 2)
        answer -= int(y1)

        # y1가 점 위로 지나갈 경우 1을 더 빼야함
        if y1 != int(y1):
            answer -= 1

    return answer * 4