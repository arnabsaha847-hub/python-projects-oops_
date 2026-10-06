def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = float(input("Enter marks: "))
    marks.append(mark)

average = sum(marks) / n
grade = calculate_grade(average)

print("Average Marks:", average)
print("Grade:", grade)