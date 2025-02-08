class Product:
    def __init__(self,name,price) ->None:
        self.__name=name
        self.set_price(price)
    def set_price(self,price):
        if (price>0):
            self.price=price
        else:
            raise ValueError("Invalid value")
p1=Product("jelly",20)
print(p1.__dict__)
# p1.set_price(-1000) will give an error
print(p1.price)
# print(p1.__name) it will give an error because it is private

        