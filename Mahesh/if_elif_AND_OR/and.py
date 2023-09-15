'''Ask the use to enter any number between 1 and 999
• If the number is not between 1 and 999 display “Invalid input”
• If the number has 1 digit, print “Input is one digit number”
• If the number has 2 digits, print “Input is two digit number”
• If the number has 3 digits, print “Input is three digit number”'''

num = int(input("Enter num between 1 and 999 : "))
if num>=1 and num<=9:
    print("Input is one digit number")
elif num>=10 and num<=99:
    print("Input is two digit number")
elif num>=100 and num<=999:
    print("Input is three digit number")
else:
    print("Invalid Input")