students = []


class Student: #Init is used for making parameters required
    
    school_name = "Vista del lago"

    def __init__(self, name, student_id=332):
        
        self.name = name
        self.student_id = student_id
        # student = {"name": name, "student_it": student_id}
        students.append(self)

    def __str__(self): #Str is used to not show class location 
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

print(Student.school_name)

# mark = Student("Mark")
# # student = Student()
# # student.add_student("Mark")
# print(mark)
    


# student = Student()

# print(student)

# new_student = Student()

# print(new_student)