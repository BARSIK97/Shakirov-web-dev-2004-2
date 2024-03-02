def compute_average_scores(scores):
    num_students = len(scores[0])
    averages = []
    for student_index in range(num_students):
        total = 0
        for subject_scores in scores:
            total += subject_scores[student_index]
        average = total / len(scores)
        averages.append(round(average, 1))
    return tuple(averages)

if __name__ == '__main__':
    n, x = map(int, input().split())
    scores = []
    for _ in range(x):
        subject_scores = list(map(float, input().split()))
        scores.append(subject_scores)
    result = compute_average_scores(scores)
    list=[]
    for avg in result:
        list.append(avg)
print(list)