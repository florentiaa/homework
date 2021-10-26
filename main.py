myList = ['knife', 'tentacle sweeper', 'lightsaber']
weapon = input(print("Choose a weapon: 1: knife"
                     "                 2: tentacle sweeper"
                     "                 3: lightsaber"))
if weapon == 'tentacle sweeper' and weapon in  myList:
    print('You chose a tentacle sweeper.')
else:
    print('Wrong weapon choice')
print(myList)
