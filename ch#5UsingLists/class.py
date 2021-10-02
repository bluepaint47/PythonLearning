from typing import AsyncGenerator


class Person:
 def __init__ (self,name,age):
    self.name = name
    self.age=age


p1 = Person("johan",36)


print(p1.name)
print(p1.age)