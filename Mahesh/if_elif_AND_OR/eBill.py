'''Create a program that calculates the electricity bill based on the units
consumed.
o The first 100 units are charged at Rs. 3 per unit,
o Units more than 100 and till 200 at Rs. 4 per unit,
o Units more than 200 and till 500 at Rs. 5 per unit
o Units more than 500 at Rs. 10 per unit'''

units = int(input("Enter Number Of Units Consumed:"))
if units<=100:
    bill=units*3
    print("Your Bill : Rs.",bill)
elif 100<units<=200:
    bill=units*4
    print("Your Bill : Rs.",bill)
elif 200<units<=500:
    bill=units*5
    print("Your Bill : Rs.",bill)
else:
    bill=units*10
    print("Your Bill : Rs.",bill)