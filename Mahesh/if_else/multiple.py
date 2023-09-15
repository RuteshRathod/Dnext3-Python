'''
Write a program to check if the user input number is a multiple of 7.
'''
num = int(input("Enter num"))
if num%7==0:
    print ("Num is multiple of 7 *",int(num/7))
else :
    print("num not a multiple of 7")