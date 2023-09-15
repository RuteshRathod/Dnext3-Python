'''Write a program to find out whether a tringle is isosceles or equilateral or scalene tringle.'''

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a==b and a==c and b==c:
    print("Triangle is Equilateral triangle")
elif a==b or a==c or b==c:
    print("Triangle is Isosceles triangle")
else:
    print("Triangle is Scalene triangle")