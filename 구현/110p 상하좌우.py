n = int(input())
moves = list(input().split())

location_y = 0
location_x = 0

for i in range(len(moves)):
    if moves[i] == "L":
        location_x = location_x-1 if location_x-1 >= 0 else location_x
    elif moves[i] == "R":
        location_x = location_x + 1 if location_x + 1 < n else location_x
    elif moves[i] == "U":
        location_y = location_y - 1 if location_y - 1 >= 0 else location_y
    elif moves[i] == "D":
        location_y = location_y + 1 if location_y + 1 < n else location_y

print(location_y+1, location_x+1)