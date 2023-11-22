class Employee:
    raise_amount=1.04
    def __init__(self,pay,email):
        self.pay=pay
        self.email=email

    def apply_raise(self):
       self.pay=int(self.pay *self.raise_amount)

class Developer(Employee):
    pass


emp_1=Employee(2000,'john@gmail.com')
emp_2=Employee(2000,'alex@gmail.com')

print(emp_1.__dict__)
print(Employee.__dict__)
print(emp_1.raise_amount)