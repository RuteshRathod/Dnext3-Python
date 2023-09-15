'''Write a program that checks if a student is eligible for admission to a
university based on their age and college percentage.
Eligibility criteria: Age between 18 and 24 (inclusive) and college
percentage more than equal to 75%.'''

age=int(input('Enter Your Age : '))
per = float(input("Enter Your Percentage : "))
if per>=75 and  18 <= age <= 24:
    print("Congratulation !!! You Eligible for Admission")
else:
    print("Sorry !!You are not eligible for Admission")