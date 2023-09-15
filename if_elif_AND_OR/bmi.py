'''Write a program that calculates a person's Body Mass Index (BMI) using
their weight (in kilograms) and height (in meters). Classify the BMI as
underweight, normal weight, overweight, or obese.
o BMI is calculated using the formula: BMI = weight / (height^2)
o BMI less than 18.5 ->; Underweight
o BMI more than equals to 18.5 and less than 24.9 ->; Normal
Weight
o BMI more than equals to 24.9 and less than 29.9
o BMI more than equal to 29.9 is obese.'''

wght =float(input ("Enter Weight "))
hgt=float(input ('Enter Height '))
bmi=(wght/(hgt**2))
if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<24.9:
    print("Normal")
elif 24.9<=bmi<29.9:
    print("Overweight")
else:
    print("obese")