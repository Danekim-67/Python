score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

total_score = 0.0
total_credits = 0.0

for _ in range(20):
    course_name, credit, grade = input().split()
    credit = float(credit)

    if grade == 'P':
        continue

    total_score += credit * score[grade]
    total_credits += credit

gpa = total_score / total_credits
print(gpa)