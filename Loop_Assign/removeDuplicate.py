'''Create a Python program that removes duplicate elements from a list,
preserving the original order. Use a for loop and a new list to accomplish
this.'''

list1 = [41,21,11,48,31,11,28,41,72]  
list2 = []
for value in list1:
    if value not in list2:
      list2.append(value)
    else:
      continue
print(list2)  