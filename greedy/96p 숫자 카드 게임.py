n, m = map(int, input().split())

data = []
maxvalue = 0
maxindex = 0

for i in range(n):
    data.append(list(map(int, input().split())))
    if min(data[i]) > maxindex:
        maxvalue = min(data[i])

print(maxvalue)

'''
# 조건문 없이
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
'''