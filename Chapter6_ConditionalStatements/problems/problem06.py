# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

grade = int(input("Enter the grade: "))


if grade >= 90 and grade < 100:
    print("Your grade is Ex")
elif grade >=80 and grade <90:
    print("Your grade is A")
elif grade >=70 and grade <80:
    print("Your grade is B")
elif grade >=60 and grade <70:
    print("Your grade is C")
elif grade >=50 and grade <60:
    print("Your grade is D")
elif grade < 50 and grade > 1:
    print("Your failed")
else:
    print("Enter valid grade")
