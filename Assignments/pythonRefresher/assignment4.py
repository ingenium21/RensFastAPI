grade = int(input("Please enter your grade (0-100): "))
letter_grade = ""
if grade >= 90:
    letter_grade = "A"
elif grade >=80:
    letter_grade = "B"
elif grade >= 70:
    letter_grade = "C"
elif grade >=60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"with a grade of {grade} your letter grade is {letter_grade}")
