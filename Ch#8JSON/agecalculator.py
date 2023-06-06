import datetime
#birth_date = datetime.time(2003,6,4)
#end_date = datetime.time(2021,11,1)
#time_diference = birth_date - end_date
#age = time_diference.days
#print(age)


year_of_birth = int(2003)
current_year = datetime.datetime.now().year
current_age = current_year - year_of_birth
print("your current age is ", current_age)

