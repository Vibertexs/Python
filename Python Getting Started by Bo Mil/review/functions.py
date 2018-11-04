# def student(name, studentid=332): #The 332 at student id makes  it optional for user input
#     print(name, studentid)
#     print(student)#or you can do this 

# student("Mark",123 )



def student(name, studentid=332): #The 332 at student id makes  it optional for user input
    students = {"name": name, "studentid": studentid}
    print(students)#or you can do this 

# student(name="Mark",studentid=123 )
student_name = input("Enter student name: ")
student_id = input("Enter students id")
# general= input()
student(student_name, student_id)
