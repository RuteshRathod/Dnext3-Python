'''1. Consider the following list:
List1 = ["Maruti","Honda","Suzuki","Ford","Renault", "Hyundai", "Kia"]
You have to ask the user to enter any car manufacturer name, and if the name is present in
the list, you have to delete that manufacturer name from the list and then print the list.
2. Consider the below list:
List1 = ["Maruti","Honda","Suzuki","Ford","Renault", "Hyundai", "Kia"]
You have to ask the user to enter any car manufacturer name, and if the name is present in
the list, you have to ask the user to enter a new car manufacturer name which would
replace the previous car manufacturer name.'''

List = ["Maruti","Honda","Suzuki","Ford","Renault", "Hyundai", "Kia"]
print("Given List : ['Maruti','Honda','Suzuki','Ford','Renault', 'Hyundai', 'Kia']")
d_r = input("Enter you want to delete(d) or replace(r): ")
if d_r=='d':
    name = input("enter any car manufacturer name: ")
    if name in List:
        List.remove(name)
        print("Deleted Successfully\n",List)
    else:
        print("Name not found")
elif d_r=='r':
    exName = input("enter existing name to replace: ")
    name = input("enter name to replace: ")
    if exName in List:
        i = List.index(exName)
        List[i] = name
        print(List)
    else:
        print("exName wrong")
else:
    print("Please Enter Correct Option")