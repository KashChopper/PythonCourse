# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# Program to check whether a student has passed or failed

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))

total_percentage = (sub1 + sub2 + sub3) / 3

if total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("Student has Passed")
else:
    print("Student has Failed")


print("_____________________________________________________________________________________________________")


marks_list = []
total_marks = 0
for i in range(3):
    marks = int(input("Marks: "))
    total_marks += marks
    marks_list.append(marks)

total_percentage = (total_marks/300) * 100

if all(marks >= 33 for marks in marks_list) and total_percentage >= 40:
    print("You passed")
else:
    print("you failed")