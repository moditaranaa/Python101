
import datetime
#Today's date:
print("Today is", datetime.date.today())

def ageCal(year,month, date):
    today = datetime.date.today()
    dob = datetime.date(year,month,date)
    age = (today-dob).days/365
    return age

    

userDob = input("Enter user DOB in 'yy/mm/dd' format : ")
dob = userDob.split('/')
year,month,date = int(dob[0]), int (dob[1]), int(dob[2])
age = ageCal(year,month,date)
print(f"You are {int(age)} years old.")
