'''You are running a promotional event for your website. 
You are going to give Rs. 75/- wallet cash to all the users who have logged in to your site from 1AM to 5AM on 15th August 2022.
You have a list of usernames who have logged in to your website:
amitk, ronitp, ravis, amitk, sonals, bipink, kamalb, rahuls, rohits, amitk, sonals, amitk, rahuls, nileshp, samirk, manishp, sonals, amitk, ravis
You have to ask your user to enter the username, and find out the amount of wallet cash he/she will receiv'''

userName = input("Enter your username : ")
List = ['amitk', 'ronitp', 'ravis', 'amitk', 'sonals', 'bipink', 'kamalb', 'rahuls', 'rohits', 'amitk', 'sonals', 'amitk', 'rahuls', 'nileshp', 'samirk', 'manishp', 'sonals', 'amitk', 'ravis']
count = List.count(userName)*75
print('Your Cashback is Rs.',count,'/-')