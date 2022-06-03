
class employee:
    def __init__(self,_name,_salary):
        self.name= _name
        self.salary= _salary

    def sayHi(self): 
        print("Hello, my name is " + self.name + " and my monthly salary is  " + self.salary)
employee1 =employee("john",str(20000))
employee1.sayHi()    

