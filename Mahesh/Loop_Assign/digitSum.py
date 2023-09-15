'''Write a program to calculate the sum of digits of a given number using a while loop.'''

num = int(input("Enter the number : "))
sumOfDigits=0
while num>0:
    rem = num%10
    sumOfDigits +=rem
    num=num//10
print(sumOfDigits)