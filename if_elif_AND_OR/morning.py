'''Write a program that takes the current hour as input and prints a
greeting message based on the entered hour: "Good morning" (5AM to
11AM), "Good afternoon" (12 PM to 4 PM), "Good evening" (5 PM to 8
PM) and "Good night" (9 PM to 4 AM)'''

hour = float(input("Enter Hour : "))
am_pm = input("Enter AM or PM : ")
if am_pm=='AM':
    if 5<=hour<12:
        print("Good Morning!")
    elif 12<=hour<5:
        print("Good Night!")
elif am_pm=='PM':
    if 5<=hour<9:
        print("Good Evening!")
    elif 12<=hour<5:
        print("Good Afternoon!")
    elif 9<=hour<12:
        print("Good Night!")
else:
    print("Invalid Input ")