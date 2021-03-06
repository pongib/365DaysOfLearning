# class Employee:
#     def __init__(self, name, email_address, title, phone_number=None, identifier=None):
#         self.name = name
#         self.email_address = email_address
#         self.title = title
#         self.phone_number = phone_number
#         self.identifier = identifier

#     def email_signature(self, include_phone=False):
#         signature = f"{self.name} - {self.title}\n{self.email_address}"
#         if include_phone and self.phone_number:
#             signature += f" ({self.phone_number})"
#         return signature

#     @classmethod
#     def get_all(cls, file_name='test_employee_file.txt'):
#         employees = []
#         with open(file_name, 'r') as my_file:
#             for index, employee in enumerate(my_file.readlines()):
#                 name, email_address, title, *phone_number = employee.split(',')
#                 phone_number = str(phone_number[0]).rstrip() if phone_number else None
#                 employees.append(cls(name, email_address, title, phone_number, identifier=index+1))
#             return employees

#     @classmethod
#     def get_at_line(cls, line_at, file_name='test_employee_file.txt'):
#         employees = []
#         with open(file_name, 'r') as my_file:
#             for index, employee in enumerate(my_file.readlines()):
#                 name, email_address, title, *phone_number = employee.split(',')
#                 phone_number = str(phone_number[0]).rstrip() if phone_number else None
#                 employees.append(cls(name, email_address, title, phone_number, index+1))
#             return employees[line_at - 1]
    
#     def save(self, file_name='test_employee_file.txt'):
#         data = f'{self.name},{self.email_address},{self.title}\n' if not self.phone_number else f'{self.name},{self.email_address},{self.title},{self.phone_number}\n'
#         if not self.identifier:
#             with open(file_name, 'a') as f:
#                 f.write(data)
#         else:
#             with open(file_name, 'r+') as f:
#                 data_list = f.readlines()
#                 data_list[self.identifier - 1] = data
#                 f.seek(0)
#                 f.writelines(data_list)



# Solution
class Employee:
    default_db_file = "employee_file.txt"

    @classmethod
    def get_all(cls, file_name=None):
        results = []

        if not file_name:
            file_name = cls.default_db_file

        with open(file_name, "r") as f:
            lines = [
                line.strip("\n").split(",") + [index + 1]
                for index, line in enumerate(f.readlines())
            ]

        for line in lines:
            print(line)
            results.append(cls(*line))

        return results

    @classmethod
    def get_at_line(cls, line_number, file_name=None):
        if not file_name:
            file_name = cls.default_db_file

        with open(file_name, "r") as f:
            line = [
                line.strip("\n").split(",") + [index + 1]
                for index, line in enumerate(f.readlines())
            ][line_number - 1]
            return cls(*line)

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

    def save(self, file_name=None):
        if not file_name:
            file_name = self.default_db_file

        with open(file_name, "r+") as f:
            lines = f.readlines()
            if self.identifier:
                lines[self.identifier - 1] = self._database_line()
            else:
                lines.append(self._database_line())
            f.seek(0)
            f.writelines(lines)

    def _database_line(self):
        return (
            ",".join(
                [self.name, self.email_address, self.title, self.phone_number or ""]
            )
            + "\n"
        )
            