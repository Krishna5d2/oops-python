class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.id)
        print("Employee Salary:", self.salary)


e1 = Employee("Krishna", 101, 25000)
e2 = Employee("chintu", 102, 30000)
e3 = Employee("ash", 103, 35000)

e1.display()
e2.display()
e3.display()