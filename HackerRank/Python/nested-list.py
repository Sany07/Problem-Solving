student = []
n=2
for _ in range(int(input())):
    name = input()
    score = float(input())
    student.append(name)
    student.append(score)

final = [student[i * n:(i + 1) * n] for i in range((len(student) + n - 1) // n)]
final.sort(key=lambda x: x[0])
final.sort(key=lambda x: x[1])

for i in range(1,2):
    print(final[i][0])
