class Employee:
    def __init__(self, name, email_address, title, phone_number=None, identifier=None):
        self.name = name
        self.email_address = email_address
        self.title = title
        self.phone_number = phone_number
        self.identifier = identifier

    def email_signature(self, include_phone=False):
        signature = f"{self.name} - {self.title}\n{self.email_address}"
        if include_phone and self.phone_number:
            signature += f" ({self.phone_number})"
        return signature

    @classmethod
    def get_all(cls, file_name='test_employee_file.txt'):
        employees = []
        with open(file_name, 'r') as my_file:
            for index, employee in enumerate(my_file.readlines()):
                name, email_address, title, phone_number = employee.split(',')
                employees.append(cls(name, email_address, title, identifier=index, phone_number=None))
            return employees

    @classmethod
    def get_at_line(cls, line_at, file_name='test_employee_file.txt'):
        employees = []
        with open(file_name, 'r') as my_file:
            for employee in my_file.readlines():
                name, email_address, title, phone_number = employee.split(',')
                employees.append(cls(name, email_address, title, phone_number=None))
            return employees[line_at - 1]
    
    def save(self, file_name='test_employee_file.txt'):
        with open(file_name, 'a') as f:
            data = f'{self.name},{self.email_address},{self.title}\n' if not self.phone_number else f'{self.name},{self.email_address},{self.title},{self.phone_number}\n'
            f.write(data)
            