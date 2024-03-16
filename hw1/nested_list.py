N = int(input())
students = []

for _ in range(N):
    name = input()
    score = float(input())
    students.append([name, score])
students.sort(key=lambda x: x[1], reverse=True)
scores = [student[1] for student in students]

m=max(scores)
a= [x for x in scores if x != m]
max_score = a[0]
splace_students = []

for student in students:
    if student[1] == max_score:
        splace_students.append(student[0])
splace_students.sort()
for student in splace_students:
    print(student)