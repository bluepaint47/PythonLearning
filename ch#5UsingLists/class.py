from typing import AsyncGenerator


class Person:
 def __init__ (self,name,age):
    self.name = name
    self.age=age

 def myFunc(self):
    print("hello my name is  " + self.name)


p1 = Person("johan",36)


print(p1.name)
print(p1.age)

p1.myFunc()