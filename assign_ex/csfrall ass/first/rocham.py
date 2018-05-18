import random
user = raw_input("Choose your weapon: ")
comp = random.choice( ['rock','paper','scissors'] )

print('the user (you) chose', user)
print('the comp (I) chose', comp)

if user == 'rock':
    print('Ha! I really chose paper -- I WIN!')
'''else:
    print('comp win')'''
if user == 'paper':
    print('win')
else:
    print('u lose')
while user=='':
    print("Still running...")
    response = input("Play again? ")
    if response == 'n':
            break
