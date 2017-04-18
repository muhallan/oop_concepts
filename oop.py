"""Demonstration of OOP concepts"""
class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class Student(Person):
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, student_type, *args, **kwargs):
        self.student_type = student_type
        self.classes = []
        super(Student, self).__init__(*args, **kwargs)

    def enrol(self, course):
        self.classes.append(course)


class StaffMember(Person):
    PERMANENT, TEMPORARY = range(2)

    def __init__(self, employment_type, *args, **kwargs):
        self.employment_type = employment_type
        super(StaffMember, self).__init__(*args, **kwargs)


class Lecturer(StaffMember):
    def __init__(self, *args, **kwargs):
        self.courses_taught = []
        super(Lecturer, self).__init__(*args, **kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)

class Course(object):
    def __init__(self, course_name):
        self.course_name = course_name


allan = Student(Student.POSTGRADUATE, "Allan", "Muhwezi", "u00667")
postgrad_course = Course("Masters in Computer Science")
allan.enrol(postgrad_course)

bob = Lecturer(StaffMember.PERMANENT, "Bob", "Mateeka", "123456789")
an_undergrad_course = Course("Bachelors of Science in Software Engineering")
bob.assign_teaching(an_undergrad_course)