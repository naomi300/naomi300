class person:
    def __init__(self,_name,_age):
        self.name = _name
        self.age = _age

    def sayHi(self):
        print("Hello, My name is " + self.name +" i am  years old " + self.age )
person1 = person("naomi", str(20))
person1.sayHi()

person2 = person("james", str(22))
person2.sayHi()

    

