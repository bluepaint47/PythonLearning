
import random
ran = random.randint(1,50)
num = 0
count = 0
while( num != ran):
        count += 1
        num = int(input("guess a number(1-50):"))
        if(num == ran):
                print("right guess" )
        elif num < ran:
                print("the number smaller")
        else:
                print("the number bigger")

print("you have guess right number in ",count, " attempts.")
