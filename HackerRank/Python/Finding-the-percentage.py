from decimal import Decimal

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
total_marks = 0
for i in student_marks[query_name]:
    total_marks += i
print(round(Decimal(total_marks/3), 2))
