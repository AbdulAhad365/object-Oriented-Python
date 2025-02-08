class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def values(self):
        print(f"Name is: {self.name} and Age is {self.age}")
p1=Person("ahad",34)
p1.values()
