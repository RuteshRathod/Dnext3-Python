'''Create a program that calculates the price of a movie ticket based on the
age of the viewer. If the viewer is under 12, the ticket costs Rs. 120/-. If
the viewer is between 12 and 65 (inclusive), the ticket costs Rs. 180/-.
Otherwise, the ticket costs Rs. 80/-.'''

age = int(input("Enter your age : "))
ticket = int(input("How many ticket you want : "))
if  age<12:
    price = ticket*120
    print("Ticket Price : Rs.",price)
elif 12<=age<=65:
    price = ticket*180
    print("Ticket Price : Rs.",price)
else:
    price = ticket*80
    print("Ticket Price : Rs.",price)
