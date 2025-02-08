class Person:
    def __init__(self,name):
        self.name=name
    def speaks(self):
        print("person speaks")

class Teacher(Person):
    def __init__(self,name,subject):
        print("Teacher speaks")
        super().__init__(name)
        self.subject=subject

class Student(Person):
    def __init__(self,name,batch):
        print("student speaks")
        super().__init__(name)
        self.batch=batch

t1=Teacher("ateeq zahoor","software engineering")
s1=Student("ahad","bcs-7a")
print(t1.name)
print(s1.name)
s1.speaks()
