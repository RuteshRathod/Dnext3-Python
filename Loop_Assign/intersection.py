'''Intersection of Lists: Write a function that finds the intersection of two
lists, i.e., common elements in both lists.'''

list1 = [41,21,11,48,31,66,28,44,72]
list2 = [48,21,44,31,44,11,66,28,26]
print(list(set(list1).intersection(set(list2))))
###################################################
# list1 = [41,21,11,48,31,66,28,44,72]  
# list2 = [48,21,44,31,44,11,66,28,26]  
# list3 = []
# for value in list1:
#    if value in list2:
#       list3.append(value)
# print(list3)  