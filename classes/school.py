from ctypes import addressof


class School:
    def __init__(self, name, address):
        self.name = name
        self.staff = []
        self.student = []
        self.address = address
    
