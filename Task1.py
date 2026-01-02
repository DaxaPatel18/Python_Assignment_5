student_details={"Daxa":99,
                 "Rishi":95,
                 "XYZ":85,
                 "ABC":78}
#print(student_details)

student=input("Enter the Student's name:")

if student in student_details:
    print(f"{student} marks: {student_details[student]}")
else:
    print("Student not found.")
