from datetime import date
import calendar
yearOfBirth=int(input("Enter year of birth: "))
monthOfBirth=int(input("Enter month of birth(1-12): "))
dayOfBirth=int(input("Enter day of birth(1-31): "))

 #program now knows the current date automatically
today=date.today()
currentYear=today.year
currentMonth=today.month
currentDay=today.day
print(f"Current date is: {currentDay}/{currentMonth}/{currentYear}")

#calculate age
years=currentYear-yearOfBirth
months=currentMonth-monthOfBirth
days=currentDay-dayOfBirth

#Fix days if negative - borrow from previous month
if days < 0:
    months -= 1
    previousMonth = currentMonth - 1 if currentMonth > 1 else 12
    prevYear = currentYear if currentMonth > 1 else currentYear - 1
    daysInPreviousMonth = calendar.monthrange(prevYear, previousMonth)[1]
    days +=daysInMonth


#Fix months if negative - borrow from previous year
if months < 0:
    years -= 1
    months += 12

print(f"You are {years} years, {months} months, and {days} days old.")
