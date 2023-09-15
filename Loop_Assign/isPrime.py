'''Prime Number Detector: Write a program that takes an integer input
and determines whether it is a prime number or not.
Prime numbers are natural numbers that are divisible by only 1 and the
number itself.
Some of the prime numbers include 2, 3, 5, 7, 11, 13, etc.'''
num = int(input("Enter the number : "))
if num>1:
    for i in range(2,int(num/2)+1):
        if num%i==0:
            print(num,"not prime")
            break
    else:
        print(num,"is prime")
else:
    print("Not Prime")