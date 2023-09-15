'''Write a program which has a list of the following roll numbers who
have passed the exam:
1223, 1235, 1239, 1241, 1244, 1254, 1259, 1260, 1273, 1289
Your program should ask the user to enter his/her roll number and
print whether he/she has passed the exam.'''

List = [1223, 1235, 1239, 1241, 1244, 1254, 1259, 1260, 1273, 1289]
rollNo = int(input("Enter Your Roll No.: "))
if rollNo in List:
    print("Congratulation !! You Passed ... ")