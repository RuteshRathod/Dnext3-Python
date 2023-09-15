'''Write a program to create a new list which will contain alternate elements of the below list:
127, 33, 46, 199, 312, 12, 55, 33, 45, 9, 310, 54
i.e. new list = 127, 46, 312, 55, 45, 310'''

List = [127, 33, 46, 199, 312, 12, 55, 33, 45, 9, 310, 54]
newList = List[::2]
print(newList)