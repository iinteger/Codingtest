'''
input
5 6
101010
111111
000001
111111
111111
'''
# 정답이 우하단이라고 단순하게 정의되어있어 왼쪽, 위쪽으로 가는 경우는 처리하지 않음.

def maze_escape(maze, y, x, step):
    if y == n-1 and x == m-1:
        print(step)
        return
    else:
        if y < 0 or y >= n or x < 0 or x >= m:
            return

    if x+1 < m and maze[y][x+1] == 1:
        maze_escape(maze, y, x+1, step+1)
    if y+1 < n and maze[y+1][x] == 1:
        maze_escape(maze, y+1, x, step+1)

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

step = 1
maze_escape(maze, 0, 0, step)