n = int(input())

student_marks = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

query_name = input()

marks_list = student_marks[query_name]
average = sum(marks_list) / len(marks_list)

print(f"{average:.2f}")