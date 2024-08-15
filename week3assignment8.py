

#Input
subject1 = float(input("Enter your grade for History Class:"))
subject2 = float(input("Enter your grade for Chemistry Class:"))
subject3 = float(input("Enter your grade for Language Arts Class:"))

#Determining the grade based on the average of the three
average_grade = (subject1 + subject2 + subject3) / 3

#Processing
if average_grade >= 90:
    grade = "A"
elif average_grade >= 80:
    grade = "B"
elif average_grade >= 70:
    grade = "C"
elif average_grade >= 60:
    grade = "D"
else:
    grade = "F"

#Display the calculated grade
print("Your average grade is:", average_grade)
print("Your grade is :", grade)
