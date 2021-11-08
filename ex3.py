password=input('Enter the correct password to continue: ')

count = 0
while password!='flo123' and count<4:
    print('Incorrect. Try again.')
    count+=1
if password == password:
    print('Correct.')
else:
    print('You lost.')
