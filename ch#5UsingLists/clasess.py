from typing import AsyncContextManager, AsyncGenerator


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

    def myfunc(self):
        print("hello my name is"+ self.name)


p1 = Person("johan",36)
p1.myfunc()