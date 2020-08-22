chemistry = int(input("Enter marks:"))
pyhsics = int(input("Enter marks:"))

if(chemistry < 30 or pyhsics < 50):
    if(chemistry < 10):
        print("come with your parrant")
    else:
        print("student fail")
elif(pyhsics > 90):
    print('student is gold medlist')
else:
    print("student pass")


