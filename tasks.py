from os import system
import datetime


users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]

users2 = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

    

def get_user(username: str, password: str, users=users):
    for user in users:
        if user['name'] == username and user['password'] == password:
            return user
    print('An error occured. You are not authorized...')
    return None


def show_offers(username: str, password: str, users=users2):
    who_is_user = get_user(username, password, users=users2)
    if who_is_user == None or who_is_user['type'] == 'Student':
        print('We have great courses to offer you!')

def isweekend(date=datetime.datetime.now()):
    if date.weekday() == 5 or date.weekday() == 6:
        return True
    else:
        return False

while True:
    system('clear')
    print('''What you want to do?
[1] - Task 1
[2] - Task 2
[3] - Task 3
[4] - Task 4
[5] - Task 5
[x] - Exit
''')
    choice = input()
    print()
    if choice == '1':
        valid = {"username": "admin", "password": "admin"}
        username = input("What is your username? ")
        password = input(f"Type the password for username {username}: ")
        if username != valid['username'] or password != valid['password']:
            print('Credentials are invalid!')
        else:
            print(f'Welcome, {username}!')

    elif choice == '2':
        print('No arguments given:', isweekend())
        print(isweekend(datetime.date(2021, 8, 6)))
        print(isweekend(datetime.date(2021, 8, 7)))
        print(isweekend(datetime.date(2021, 8, 8)))
        print(isweekend(datetime.date(2021, 8, 9)))
    elif choice == '3':
        valid = {"username": "admin", "password": "admin"}
        username = input("What is your username? ")
        password = input(f"Type the password for username {username}: ")
        today = datetime.date(2021, 8, 7)
        if (username != valid['username'] or password != valid['password']) and isweekend(today) == False:
            print('Credentials are invalid!')
        else:
            print(f'Welcome, {username}!')
    elif choice == '4':
        print(get_user(input('Insert username: '), input('Insert password: ')))
    elif choice == '5':
        show_offers(input('Insert username: '), input('Insert password: '))
    if choice != 'x':
        print()
        input('Press Enter to continue...')
        continue
    else:
        print("Alright, see you!")
        break
