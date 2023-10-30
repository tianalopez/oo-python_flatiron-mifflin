from lib.employee import Employee

class Manager:
    all=[]
    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age

        type(self).all.append(self)

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
    def department(self):
        return self._department
    @department.setter
    def department(self, new_department):
        if not isinstance(new_department, str):
            raise TypeError("Need to input string")
        else: self._department = new_department

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError("Need to input integer")
        else:
            self._age = new_age

    def employees(self):
        return [employee for employee in Employee.all
                if employee.manager_name == self.name]

    def hire_employee(self, employee_name, employee_salary):
        self.employees().append(Employee(employee_name, employee_salary))

    @classmethod
    def all_departments(cls):
        return list({manager.department for manager in cls.all})

    @classmethod
    def average_age(cls):
        manager_list = [manager.age for manager in cls.all]
        return float(sum(manager_list)/len(manager_list))
