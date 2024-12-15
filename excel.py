class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def register_course(self, course):
        self.courses.append(course.title)

    def display_info(self):
        return f'Student: {self.name} (ID: {self.student_id}), Courses: {", ".join(self.courses)}'


class Professor:
    def __init__(self, name, professor_id):
        self.name = name
        self.professor_id = professor_id
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course.title)

    def display_info(self):
        return f'Professor: {self.name} (ID: {self.professor_id}), Courses: {", ".join(self.courses)}'


class Course:
    def __init__(self, code, title):
        self.code = code
        self.title = title
        self.professor = None
        self.students = []

    def assign_professor(self, professor):
        self.professor = professor
        professor.assign_course(self)

    def register_student(self, student):
        self.students.append(student)
        student.register_course(self)

    def display_info(self):
        professor_name = self.professor.name if self.professor else "No professor assigned"
        s = [student.name for student in self.students]
        return f'Course: {self.title} (Code: {self.code}), Professor: {professor_name}, Students: {", ".join(s)}'


class University:
    def __init__(self):
        self.students = {}
        self.professors = {}
        self.courses = {}

    def add_student(self, name, student_id):
        student = Student(name, student_id)
        self.students[student_id] = student

    def add_professor(self, name, professor_id):
        professor = Professor(name, professor_id)
        self.professors[professor_id] = professor


    def add_course(self, code, title):
        course = Course(code, title)
        self.courses[code] = course

    def assign_professor_to_course(self, course_code, professor_id):
        if course_code in self.courses and professor_id in self.professors:
            course = self.courses[course_code]
            professor = self.professors[professor_id]
            course.assign_professor(professor)

    def register_student_to_course(self, course_code, student_id):
        if course_code in self.courses and student_id in self.students:
            course = self.courses[course_code]
            student = self.students[student_id]
            course.register_student(student)

    def display_student_info(self, student_id):
        if student_id in self.students:
            return self.students[student_id].display_info()

    def display_professor_info(self, professor_id):
        if professor_id in self.professors:
            return self.professors[professor_id].display_info()

    def display_course_info(self, course_code):
        if course_code in self.courses:
            return self.courses[course_code].display_info()

    def display_all_courses(self):
        return [course.display_info() for course in self.courses.values()]


def main():
    university = University()
    while True:
        command = input("Enter command and values: ").strip().split()

        if command[0] == "add_student":
            name = command[1]
            student_id = int(command[2])
            university.add_student(name, student_id)

        elif command[0] == "add_professor":
            name = command[1]
            professor_id = int(command[2])
            university.add_professor(name, professor_id)

        elif command[0] == "add_course":
            code = command[1]
            title = ' '.join(command[2:])
            university.add_course(code, title)

        elif command[0] == "assign_professor_to_course":
            course_code = command[1]
            professor_id = int(command[2])
            university.assign_professor_to_course(course_code, professor_id)

        elif command[0] == "register_student_to_course":
            course_code = command[1]
            student_id = int(command[2])
            university.register_student_to_course(course_code, student_id)

        elif command[0] == "display_student_info":
            student_id = int(command[1])
            print(university.display_student_info(student_id))

        elif command[0] == "display_professor_info":
            professor_id = int(command[1])
            print(university.display_professor_info(professor_id))

        elif command[0] == "display_course_info":
            course_code = command[1]
            print(university.display_course_info(course_code))

        elif command[0] == "display_all_courses":
            courses_info = university.display_all_courses()
            for info in courses_info:
                print(info)

        elif command[0] == "exit":
            break


main()