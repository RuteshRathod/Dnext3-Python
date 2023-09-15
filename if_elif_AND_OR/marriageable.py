'''Write a program to accept gender (male/female) and age as input
and display whether the user is of marriageable age.
• If gender is male, marriageable age is 21 years
• If gender is female, marriageable age is 18 years'''

gender=input("Enter gender: ")
age = int(input("Enter age: "))
if (gender=="male" and age>=21) or (gender=="female" and age>=18):
        print ("Your age is marriageable")
else:
       print ("Your age is not marriageable")