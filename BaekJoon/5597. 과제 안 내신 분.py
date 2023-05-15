student_list = [i + 1 for i in range(30)]

for _ in range(28):
    student_list.remove(int(input()))

for student in student_list:
    print(student)
