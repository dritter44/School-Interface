from Person_class import Person

class Student(Person):
    def __init__(self, name, age, role, password, student_id):
        super().__init__(name, age, role, password)
        self.student_id = student_id


student_info = {'name': 'Diana', 'password': 'password', 'school_id': 12345, 'age': 17, 'role': 'Student'}
diana = Student(**student_info)
