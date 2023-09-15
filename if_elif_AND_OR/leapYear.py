'''Write a program to find out whether an input year is a leap year or not.'''

year = int(input("Enter the Year: "))
if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)): 
    print("Given Year is a leap Year")
else:
    print("Not a leap Year")