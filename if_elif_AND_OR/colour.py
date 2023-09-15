'''Write a program to input colour of the traffic light.
• If light colour is red, inform the user to stop
• If the light colour is orange, inform the user to slow down.
• If the light colour is green, inform the user to move on
• Otherwise inform the user that input is invalid.'''

color = input("Enter traffic light color\n(red,orange,green): ")
if color=='red':
    print("STOP")
elif color=='orange':
    print("SLOW DOWN")
elif color=='green':
    print("MOVE ON")
else:
    print('invalid input')