input = input()
x = ord(input[0])-96
y = int(input[1])

moves = [[1, 2],[2, 1],[2, -1],[1, -2],[-1, -2],[-2, -1],[-2, 1],[-1, 2]]

count = 8
print([x, y])
for i in moves:
    if (0 in [x+i[0], y+i[1]]) or (-1 in [x+i[0], y+i[1]]) or (9 in [x+i[0], y+i[1]]) or (10 in [x+i[0], y+i[1]]):
        count -= 1

print(count)