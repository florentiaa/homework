print('Enter correct password to continue: ')
count=0
while count < 3:
    password = input('Enter password: ')
    if password=='flo123':
        print('Correct Password.')
        break
    else:
        print('Incorrect password. Try again.')
        count += 1

print("You lost.")
