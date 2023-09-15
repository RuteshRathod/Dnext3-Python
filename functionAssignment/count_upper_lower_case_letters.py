def count_upper_lower_case_letters(s):
    return (len([c for c in s if 'a' <= c and c <='z']),len([c for c in s if 'A'<= c  and c<='Z']))

s = input("Enter String : ")
lower_case,upper_case = count_upper_lower_case_letters(s)
print("Number of upper case letters: ",upper_case)
print("Number of lower case letters: ",lower_case)