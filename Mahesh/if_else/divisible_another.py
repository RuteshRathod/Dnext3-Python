'''
Create a program that checks if a given number is divisible by another
number (e.g., check if 10 is divisible by 5). You can take both the
numbers as user input.
'''
x=int(input('Enter x'))
y=int(input('Enter y'))
if x%y==0:
    print(x,"Divisible by",y)
else:
    print(x,"not Divisible by",y)