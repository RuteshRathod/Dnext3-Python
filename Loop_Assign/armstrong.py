'''Write a program to print all Armstrong numbers less than a given
number.
Armstrong numbers: A number that is equal to the sum of its own digits
raised to the power of the number of digits in the number itself.
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153'''

n=int(input("Enter start no. "))
n1=int(input("Enter stop no. "))
for num in range(n,n1+1):
    sum=0
    temp=num 
    while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
            print(num)      