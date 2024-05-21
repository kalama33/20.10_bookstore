import numpy as np

# 2d, 4x3, random numbs. between 50 and 100+

array = np.random.randint(50, 101, size= (4,3))

# mean scores for subject, axis 0 columns

subject_means = np.mean(array, axis=0)

# mean scores for students, axis 1, row

student_means = np.mean(array, axis=1)

# print mean scores for subject 

subjects = ["Math", "Science", "History"]
for i, subject in enumerate(subjects):
    print(f"Subject: {subject}, Mean Score: {subject_means[i]}")
    
# print the mean scores for each student

for i , mean_score in enumerate(student_means):
    print(f"Student {i}, Mean Score: {mean_score}")