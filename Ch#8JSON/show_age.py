import datetime
current_date = datetime.datetime.now()
deadline = input ('4,6,2004')
deadlineDate = datetime.datetime.strptime(deadline, '%m/%d/%Y') 
print(deadline)
daysLeft = deadlineDate - current_date
print(daysLeft)

years = ((daysLeft.total_seconds())/(365.242*24*3600))
yearsInt = int(years)

months = (years-yearsInt)*12
monthsInt=int(years)

days = (months-monthsInt)*(365.242*3600)
daysInt = int(days)
print("you are ",yearsInt,monthsInt,daysInt)



