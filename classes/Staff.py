from Person_class import Person

class Staff(Person):
    def __init__(self, name, age, role, password, employee_id):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

staff_info = {'name': 'Ethel', 'password': 'password', 'employee_id': 67891, 'age': 57, 'role': 'Staff'}
diana = Staff(**staff_info)