n, m = map(int, input().split())
arr = [20000]*10001  # 인덱스만큼의 가격에 도달하기 위한 최소 갯수

money = []
for i in range(n):
    a = int(input())
    money.append(a)
    arr[a] = 1

money.sort()

# 화폐 종류에 따라 만들 수 있는 금액과 만들 수 없는 금액이 있음

# 9 : 4 + 5
for i in range(n):
    for j in range(money[i], m+1):  # 가지고 있는 화폐들로 조합할 수 있는지 체크
        arr[j] = min(arr[j], arr[j-money[i]]+1)

if arr[m] == 20000:
    print(-1)
else:
    print(arr[m])