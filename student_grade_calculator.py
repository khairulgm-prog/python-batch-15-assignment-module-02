#PythonBatch14Module02Assignment submitted by Md Khairul Alam Prodhan

#Student Grade Calculator

# 1. Take the student's name as input

student_name = input("Enter the student's name: ")

# 2. Take marks for 3 subjects

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# 3. Calculate total and average marks

total_marks = mark1 + mark2 + mark3
average_marks = total_marks / 3

# 4. Determine the grade based on the average

if 80 <= average_marks <= 100:
    grade = "A+"
elif 70 <= average_marks < 80:
    grade = "A"
elif 60 <= average_marks < 70:
    grade = "B"
elif 50 <= average_marks < 60:
    grade = "C"
elif 0 <= average_marks < 50:
    grade = "F"
else:
    grade = "Invalid Marks"

# 5. Display the result using an f-string

print("\n--- Student Result ---")
print(f"Student Name : {student_name}")
print(f"Total Marks  : {total_marks:.2f}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Final Grade  : {grade}")
