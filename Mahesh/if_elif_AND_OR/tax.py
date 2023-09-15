'''Write a program to calculate income tax of a person. Your program should ask the user his/her annual income.
• The tax should be calculated as per the tax slabs given in this slide.'''
income = int(input("Enter annual income: "))
if 0<=income<=300000:
    print("No Tax")
elif 300000<=income<=500000:
    tax = income*0.05
    print("You have to pay",tax,"Tax")
elif 500000<=income<=750000:
    tax = income*0.1
    print("You have to pay",tax,"Tax")
elif 750000<=income<=1000000:
    tax = income*0.15
    print("You have to pay",tax,"Tax")
elif 1000000<=income<=1250000:
    tax = income*0.20
    print("You have to pay",tax,"Tax")
elif 1250000<=income<=1500000:
    tax = income*0.25
    print("You have to pay",tax,"Tax")
else:
    tax = income*0.3
    print("You have to pay",tax,"Tax")