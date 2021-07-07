# set 및 2중 반복문으로 풀면 더 간단하게 풀 수 있음!

import sys


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True

        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid + 1

    return False


n = int(input())
store = list(map(int, sys.stdin.readline().split()))
m = int(input())
customer = list(map(int, sys.stdin.readline().split()))

store.sort()

for i in customer:
    if binary_search(store, i, 0, len(store)-1):
        print("yes")
    else:
        print('no')