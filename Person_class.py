#creating the person class, that will hold the shared attributes of the staff and student classes
class Person:
    def __init__(self, name, age, role, password):
        self.name = name
        self.age = age
        self.role = role
        self.password = password
        