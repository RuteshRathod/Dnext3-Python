'''Build a basic calculator that performs addition, subtraction,
multiplication, or division based on user input. Handle cases when the
user enters an invalid operator.
Here you have to take the following inputs:
o Two numbers to perform the operation.
o The operation to perform (+,-,*,/)'''

num1 = float(input("Enter Num 1"))
num2 = float(input("Enter Num 2"))
oprtr = input("Enter Operator + - * / ")
if oprtr == '+':
    print(f"{num1}+{num2}={num1+num2}")
elif oprtr == '-':
    print(f"{num1}-{num2}={num1-num2}")
elif oprtr == '*':
    print(f"{num1}*{num2}={num1*num2}")
elif oprtr == '/':
    print(f"{num1}/{num2}={num1/num2}")
else:
    print("Invalid Input!")