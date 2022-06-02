from unicodedata import name


class employee:
    def __init__(self,_name,_salary):
        self.name= _name
        self.salary= _salary

    def sayHi(self): 
        print("hello, my name is "+ self.name + "my monthly salary is  " + self.salary)
employee1 = ("james",())
employee1.sayhi()    
