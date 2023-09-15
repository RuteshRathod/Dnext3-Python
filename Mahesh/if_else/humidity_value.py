'''
Take user input for humidity value, if the humidity is more than 75, then
inform the user that there will be rain, otherwise inform that there will
be a sunny day.
'''
humidity_value=float(input("Enter Humidity Value"))
if humidity_value>75:
    print("there will be rain")
else:
    print("there will be a sunny day")