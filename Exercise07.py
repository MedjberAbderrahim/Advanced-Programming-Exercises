year = int(input("Please type in a year: "))

if( (not (year % 4) and (year % 100)) or (not (year % 100) and not (year % 400))):
    print("That year is a leap year.")
else:
    print("That year is not a leap year")