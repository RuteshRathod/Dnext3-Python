'''Print all the perfect squares less than a given number.
A perfect square is a number that can be obtained by squaring an
integer. For example, 16 is a perfect square because it is equal to 4^2.
e.g. if the given number is 10, then the perfect squares are 1, 4 and 9'''

num=int(input("Etner Starting Number "))
num1=int(input("Enter Last Number " ) )
print('Perfect square between Two Number : ',end=' ')
while num<=num1:
    for i in range(1,num):
        if i*i==num:
            print(num, end=' ')
    num+=1