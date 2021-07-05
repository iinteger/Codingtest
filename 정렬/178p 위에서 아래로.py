n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
    print(i, end=" ")