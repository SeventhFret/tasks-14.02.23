from os import system


while True:
    system('clear')
    print('''What you want to do?
[1] - Task 1
[2] - Task 2
[3] - Task 3
[4] - Task 4
[x] - Exit
''')
    choice = input()
    print()
    if choice == '1':
        print('Shit 1')
    elif choice == '2':
        print('Shit 2')
    elif choice == '3':
        print('Shit 3')
    if choice != 'x':
        print()
        input('Press Enter to continue...')
        continue
    else:
        print("Alright, see you!")
        break
