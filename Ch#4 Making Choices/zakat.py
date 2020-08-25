nisab = 46329
num = 1
while num == 1:
    amount = int(input("Enter amount (pkr) :"))
    if  amount >= nisab : 
        zakat = amount /40 
        print("You are eligible for Zakat and your Zakat is " + str(zakat))
    else:
        print("You are not eligible for Zakat")
