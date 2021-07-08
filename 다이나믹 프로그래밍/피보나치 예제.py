# 재귀
'''
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4))
'''

'''
# 한번 계산한 결과를 메모이제이션하기 위한 리스트
d = [0]*100
# 피보나치 함수 (탑다운 DP)
def fibo(x):
    if x ==1 or x ==2:
        return 1

    if d[x] != 0:
        return d[x]  # 한번 계산된 결과는 바로 반환 O(1), 재귀에서는 다시  fibo()를 호출해 계산했었음

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
'''

# 바텀업 DP
d = [0]*100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])