# define class

class Student:
    def __init__(self, name, age): # no courses
        self.name = name
        self.age = age
        self.courses = []
        
# methods

    def enroll(self, course):
        self.courses.append(course)
        
    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{self.name} is not enrolled in {course}.")
        
    def list_courses(self):
        if not self.courses:
            return "No courses enrolled"
        else:
            course_list = ",".join(self.courses)
        return f"The student is enrolled in {course_list}"
    
# info method

    def __str__(self):
        return f"The student {self.name}, is {self.age} years old and is enrolled in {self.courses}"

# instance

student_1 = Student("Papaya","25")

student_1.enroll("Math")
student_1.enroll("C.S")

print(student_1)
print(student_1.list_courses())