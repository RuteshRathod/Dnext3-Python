usernames = {"maheshtawar","pratikmalas","nileshtawar","kishor","sanika","pragati","shruti"}
print("***************************** Remove Username Process *****************************")
userInput = input("Enter Username : ")
try:
    usernames.remove(userInput)
except Exception as e:
    print("Please Enter Valid Username",e)
else:
    print("Remove Successfully !!! ")