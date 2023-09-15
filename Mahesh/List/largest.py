'''Write a program to find the largest number in the below list:
127, 33, 46, 199, 312, 12, 55, 33, 45, 9, 310, 54'''

List = [127, 33, 46, 199, 312, 12, 55, 33, 45, 9, 310, 54]
List.sort(reverse=True)
print("Largest: ",List[0])