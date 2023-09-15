'''Create a program that takes a person's age as input and classifies them
as a child (0-12), teenager (13-19), adult (20-64), or senior (65 and
older). Depending on input age you have to print whether the person is
child / teenager / adult / senior.'''

age = int(input("Enter your age"))
if  0 <= age < 13:
    print('Child')
elif 13 <= age < 20:
    print('teenager')
elif 20 <= age < 65:
    print('teenager')
else:
    print('senior')