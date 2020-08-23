
list = input("Enter numbers")
for character in list:
    num = int(character)
    if (num % 2 == 0):
     print(num," is even")
    else:
     print(num," is odd")
