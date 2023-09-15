'''Create a program that takes three numbers as input and finds the maximum among them.'''

num=[]
i=0
while i<3:
    num1=float(input(f"Enter number {i+1} : "))
    num.append(num1)
    i+=1
num.sort()
print("Max number is :",num[-1])