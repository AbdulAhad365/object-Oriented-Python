class A:
    def info(self):
        print("Class A")

class B(A):
    def info(self):
        print("CLASS b")
class C(A):
    def info(self):
        print("class C")
class D(C,B):
    pass

d1=D()
d1.info()     # or 
# D().info()

# check how the isinstance / issubclass work
print(isinstance(d1,D)) # d1 is instance of the class D
print(issubclass(B,A))
