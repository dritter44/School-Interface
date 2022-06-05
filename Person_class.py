#creating the person class, that will hold the shared attributes of the staff and student classes
class Person:
    def __init__(self, name, age, role, password):
        self.name = name
        self.age = age
        self.role = role
        self.password = password

class Staff(Person):
    def __init__(self, name, age, role, password, employee_id):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

class Student(Person):
    def __init__(self, name, age, role, password, student_id):
        super().__init__(name, age, role, password)
        self.student_id = student_id


