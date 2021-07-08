x = int(input())

d = [0] * (x+1)
# 26 25 5 1
for i in range(2, x+1):

    d[i] = d[i-1]+1  # 1을 빼는 경우를 먼저 계산해놓고, 나눗셈 연산이 더 효율적이면 바꿈

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)  # 뺄셈 한 결과와 나눗셈 한 결과 중 더 좋은 결과를 적용
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
