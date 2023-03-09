# Loop Exercises
switch = True
while (switch == True):
    print('Hello World!')
    cont = input('Would you like to continue (y/n)? ')
    if cont == 'n':
        switch = False
        break

locked = True

def tries(num):
    tries = num
    while tries >= 0:
        keycode = input('Please enter keycode: ')
        if keycode == '13579':
            print('Welcome...')
            break
        else:
            print('Incorrect code, please try again.')
            print(f'You have {tries} tries remaining.')
            tries -= 1
            if(tries == 0):
                print('You have no tries remaining. Account has been locked.')
                locked = False  # forces loop to stop
                break



while locked == True:
    tries(5)
    break