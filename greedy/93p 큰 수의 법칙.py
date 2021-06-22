
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

sum = 0
count = 0

finish = False
while True:
    for i in range(k):
        if count == 8:
            finish = True
            break
        sum += data[-1]
        count += 1

    if finish == True:
        break
    sum += data[-2]
    count += 1

print(sum)

'''
# 반복되는 수열을 사용한 풀이
# k+ 1의 수열이 반복됨

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

sum = 0
count = int(m / (k+1))
remain = m % ((k+1))

sum += data[-1] * (count*k + remain)
sum += count * data[-2]

print(sum)
'''
