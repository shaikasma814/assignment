from datetime import datetime
name=input("Enter you name:\t")
age=int(input("Enter age:\t"))
fyear=int((100-age) + datetime.now().year)
print(fyear)
print ('Hello %s. You are %s years old. You will turn 100 years old in %s.' %(name,age,fyear))