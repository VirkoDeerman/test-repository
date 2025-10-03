from random import randint

print(f'\nGuess a number from 1 to 100')
while True:
    goal = randint(1, 100)
    while True:
        if usput:= input('> '):
            try:
                usput = int(usput)
            except ValueError:
                print('\nHey! You didn\'t enter a number! Try again.')
                continue

            if usput == goal:
                print('\nCongratulations! You won!\nGenerating new number...\n\nNew number generated. Try to guess it too!')
                break
            else:
                print(f'\nKEEP. GAMBLING.\nThe number is {'lower' if usput > goal else 'bigger'}.')
        else:
            usput = input('\nConfirm exit\n> ')
            if not usput if not usput else usput[0] in 'ye':
                raise SystemExit
            print()
