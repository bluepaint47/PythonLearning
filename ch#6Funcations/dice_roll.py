
import random



def roll_dice(dice):
    num = 0
    for rolls in range(0,dice):
        num += random.randint(1,6)
    return num
diceNum = 3
p1 = roll_dice(diceNum)
p2 = roll_dice(diceNum)
p3 = roll_dice(diceNum)
p4 = roll_dice(diceNum)
print("P1:",p1)
print("P2:",p2)
print("P3:",p3)
print("P4:",p4)


