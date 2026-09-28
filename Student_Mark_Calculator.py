print("------ STUDENT MARKS CALCULATOR ------")

Name = input("Enter your name:")

English = int(input("Enter your English marks:"))
Maths = int(input("Enter your Maths marks:"))
Physics = int(input("Enter your Physics marks:"))
Chemistry = int(input("Enter your Chemistry marks:"))
Computer_Science = int(input("Enter your Computer Science marks:"))

Total_marks = English+Maths+Physics+Chemistry+Computer_Science

Percentage = (Total_marks/5)

if Percentage >= 90:
    Grade = "A+"
elif Percentage >= 80:
    Grade = "A"
elif Percentage >= 70:
    Grade = "B"
elif Percentage >= 60:
    Grade = "C"
else:
    Grade = "F"

if Maths >= 35 and English >= 35 and Physics >= 35 and Chemistry >= 35 and Computer_Science >= 35:
    result = "Pass"
else:
    result = "Fail"

print("------ STUDENT MARKS REPORT ------")

print("Student Name:",Name)
print("Total Marks:",Total_marks)
print("Percentage:",Percentage)
print("Grade:",Grade)
print("Result:",result)

print("----- END OF REPORT -----")


