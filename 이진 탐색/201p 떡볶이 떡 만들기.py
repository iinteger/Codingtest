import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(arr)

best = 0
while start <= end:
    mid = (start+end) // 2  # h

    arr2 = [i-mid for i in arr if i > mid]
    total = sum(arr2)

    # 요구량보다 떡이 더 많이 잘렸으면 -> mid를 높여야 함, 일단 답이 될 수 있음
    if total >= m:
        best = mid
        start = mid+1

    # 요구량보다 떡이 더 적게 잘렸으면 -> mid를 낮춰야 함
    elif total < m:
        end = mid -1

print(best)

'''
# 나쁜 풀이 (n의 최댓값이 1000000, m의 최댓값이 2000000000, 떡의 개별 높이 최대값이 10억이기 때문)
n, m = map(int, input().split())
arr = list(map(int, input().split()))

h = max(arr)
while h > 0:
    arr2 = [i-h for i in arr if i> h]

    if sum(arr2) >= m:
        print(h)
        break
    h -= 1
'''