import numpy as np

marks = np.array([
    [78, 84, 69],
    [90, 88, 77],
    [65, 70, 60],
    [82, 79, 85],
    [72, 74, 68]
])

# Calculate the average score of each student (row-wise mean)
student_averages = np.mean(marks, axis=1)
print("Average score of each student:", student_averages)

# Calculate average score per subject (column-wise mean)
subject_averages = np.mean(marks, axis=0)
print("Average score per subject:", subject_averages)

# Find the highest score in the entire matrix
highest_score = np.max(marks)
print("Highest score in the matrix:", highest_score)

# Which student scored the highest overall?
student_totals = np.sum(marks, axis=1)
highest_student_index = np.argmax(student_totals)
print("Student with the highest overall score (by total):", highest_student_index, "with total:", student_totals[highest_student_index])