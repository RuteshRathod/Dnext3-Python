def is_leap_year(year):
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)): 
        return True

year = int(input("Enter year : "))
if (is_leap_year(year)):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
