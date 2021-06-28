n, m = map(int, input().split())

icebox = []
for i in range(n):
    icebox.append(input())

icecream = []
icecream_count = 0
def dfs_icecream(icebox, i, j):
    icecream.append((i, j))

    if j+1 < m:
        if icebox[i][j+1] == "0" and (i, j+1) not in icecream:
            dfs_icecream(icebox, i, j+1)
    if i+1 < n:
        if icebox[i+1][j] == "0" and (i+1, j) not in icecream:
            dfs_icecream(icebox, i+1, j)
    if j-1 > 0:
        if icebox[i][j-1] == "0" and (i, j-1) not in icecream:
            dfs_icecream(icebox, i, j-1)
    if i-1 > 0:
        if icebox[i-1][j] == "0" and (i-1, j) not in icecream:
            dfs_icecream(icebox, i-1, j)

for i in range(n):
    for j in range(m):
        if icebox[i][j] == "0" and (i, j) not in icecream:
            dfs_icecream(icebox, i, j)
            icecream_count += 1

print(icecream_count)