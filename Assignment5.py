n = int(input("Enter number of students: "))

class_total = 0

for i in range(n):
    total = 0

    print("Student", i + 1)

    for j in range(5):
        marks = int(input("Enter marks: "))
        total = total + marks

    average = total / 5
    print("Average =", average)

    class_total = class_total + total

class_average = class_total / (n * 5)

print("Overall class average =", class_average)