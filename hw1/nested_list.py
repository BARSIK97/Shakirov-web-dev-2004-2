N = int(input())
students = []
for _ in range(N):
    name = input()
    score = float(input())
    students.append([name, score])
students.sort(key=lambda x: x[1], reverse=True)

scores = [student[1] for student in students]

second_max_score = scores[1]

second_max_students = []
for student in students:
    if student[1] == second_max_score:
        second_max_students.append(student[0])

second_max_students.sort()

for student in second_max_students:
    print(student)
