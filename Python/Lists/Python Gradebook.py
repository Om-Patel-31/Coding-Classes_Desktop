ast_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
#1
subjects = ["physics", "calculus", "poetry", "history"]
#2
grades = [98, 97, 85, 88]
# 5
subjects.append("computer science")
grades.append(100)
#3
gradebook = list(zip(subjects, grades))
# 6
gradebook.append(("visual arts", 93))
#4
print(gradebook)
#print
print()
#7
full_gradebook = ast_semester_gradebook + gradebook
print(full_gradebook)