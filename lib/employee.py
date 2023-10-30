class Employee:
    all = []
    def __init__(self, name, salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager

        type(self).all.append(self)

    def tax_bracket(self):
        return [employee for employee in self.all
                if self.salary - 1000 <= self.salary <= self.salary + 1000]

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Need to input string")
        else:
            self._name = new_name

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, int):
            raise TypeError("Need to input integer")
        else:
            self._salary = new_salary

    def manager_name(self):
        return self.manager.name

    @classmethod
    def paid_over(cls, salary_comp):
        return [employee for employee in cls.all
                if employee.salary > salary_comp]

    @classmethod
    def find_by_department(cls, department):
        if not isinstance(department, str):
            raise TypeError("Department must be a string")
        else:
            employees = [employee for employee in cls.all
                        if employee.manager.department == department]
            if employees[0]:
                return employees[0]
            else:
                raise IndexError("No employee exists")
