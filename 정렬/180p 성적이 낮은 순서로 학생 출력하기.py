n = int(input())

students = []
for i in range(n):
    student = input()
    name = student.split(" ")[0]
    score = int(student.split(" ")[1])

    students.append((student.split(" ")[0], int(student.split(" ")[1])))

students.sort(key=lambda x:x[1])

for i in students:
    print(i[0], end=" ")