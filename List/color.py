'''You have to ask your first friend for 3 colours s/he loves. Create a list from the friend’s
favourite colours. Ask your second friend about his/her most favourite colour, if the second
friend’s favourite colour matches with any colour your first friend likes, then you have to
print the common colour.'''    

frnd1 = []
frnd2 = []
def takeColor(frnd,name):
    i=0
    while i<3:
        color=input(f'Enter {name} Favourite Colour {i+1}: ')
        frnd.append(color)
        i+=1
    print(name,"your Fav Colors :",frnd)

takeColor(frnd1,'Mahesh')
takeColor(frnd2,'Nilesh')
# print(frnd2)

c = 0
commonColor = []
while c<len(frnd2):
    if frnd2[c] in frnd1:
        commonColor.append(frnd2[c])
        # print("Common Color:",frnd2[c])
    c+=1

if len(commonColor) != 0:
    print("Common Color:",commonColor)
else:
    print("No Common Color")