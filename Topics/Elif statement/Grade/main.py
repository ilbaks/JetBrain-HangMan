student_score = int(input())
max = int(input())
percentage = (student_score / max) * 100
if percentage >= 90:
    print("A")
elif percentage >= 80:
    print("B")
elif percentage >= 70:
    print("C")
elif percentage >=60:
    print("D")
else:
    print("F")
