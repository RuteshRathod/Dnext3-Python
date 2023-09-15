def replace_substring(inputS,old,new):
    return inputS.replace(old, new)

inputS = input("Enter String : ")
old = input("Enter subString which replace: ")
new = input("Enter new subString to replace : ")
print ("Original string is ", inputS )  #original string
print ( "New string with replaced substring is \"", replace_substring(inputS , old , new),"\"")