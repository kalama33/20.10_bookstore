scores = [[50, 78, 64 ], 
          [22, 57, 70],
          [88, 86, 72],
          [60, 60, 73]]

student_means = []

for student_scores in scores:
    average = sum(student_scores)/ len(student_scores)
    student_means.append(average)

student_means =  [sum(student_scores) / len(student_scores) for student_scores in scores]   

print(student_means)

subject_means = []

students = ["student1", "student2", "student3", "student4"]
subjects = ["Math", "Science", "History"]

for col, subject in enumerate(subjects):
    sum_subject = 0
    print(subject)
    for row, student in enumerate(students):
        print(scores[row][col])
        sum_subject += scores[row][col]
        
    subject_means.append(sum_subject/len(students))

print(subject_means)

# print(scores)

scores_t = list(zip(*scores))

# print(scores_t)

subject_means = [sum(subject_score) / len(subject_score) for subject_score in scores_t]

print(subject_means)


