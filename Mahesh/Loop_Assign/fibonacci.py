'''Fibonacci Series: Write a program to generate the Fibonacci series up to
the user input number.
The Fibonacci series is a sequence in which each number is the sum of
the two preceding ones.
e.g. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144'''

num = int(input("Enter the number : "))
num1 = 0
num2 = 1
print('fibonnaci series : ',num1,num2,end=' ')
for i in range(2,num):
    print(num1+num2,end=' ')
    num1,num2 = num2,(num1+num2)