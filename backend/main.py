from time import sleep
import mysql.connector as sqltor
from game import *

# Connection
con = sqltor.connect(
    host='localhost',
    user='root',
    passwd='_____',   
    database='CVDB'
)
cur = con.cursor()

def checkPwd(user, pwdE):
    cur.execute('SELECT pwd FROM Accounts WHERE user=%s', (user,))
    pwd = cur.fetchone()
    if pwd and pwd[0] == pwdE:
        return True
    return False

def user_exists(U):
    cur.execute('SELECT pwd FROM Accounts WHERE user=%s', (U,))
    A = cur.fetchall()
    return len(A) != 0

def login():
    U = input('Enter Username: ')
    if user_exists(U):
        passwd = input('Enter Password: ')
        if checkPwd(U, passwd):
            return U
        else:
            print("Incorrect password.")
    else:
        print("Username does not exist.")
    return U

def add_account():
    Uname = input('Username: ')
    if user_exists(Uname):
        print('Account with entered username already exists\nLogin - L \nEnter another username - U ')
        inp = input().strip().upper()
        if inp == 'L':
            login()
        else:
            add_account()
    else:
        pwd = input('Password: ')
        cur.execute("INSERT INTO Accounts (user, pwd) VALUES (%s, %s)", (Uname, pwd))
        con.commit()
        print('Account created successfully')
        return Uname

def retrieveLevel(user):
    cur.execute("SELECT Lv, subLv FROM Accounts WHERE user=%s", (user,))
    A = cur.fetchone()
    return A

def incrLevel(user):
    B = retrieveLevel(user)
    if B[1] < 4:
        cur.execute('UPDATE Accounts SET subLv=subLv+1 WHERE user=%s', (user,))
    elif B[1] == 4 and B[0] < 4:
        cur.execute('UPDATE Accounts SET Lv=Lv+1, subLv=1 WHERE user=%s', (user,))
    elif B[0] == 4 and B[1] == 4:
        print('You have successfully saved your account.')
        return True
    con.commit()

def lives(user):
    cur.execute("SELECT lives FROM Accounts WHERE user = %s", (user,))
    A = cur.fetchone()
    return A[0]

def is_completed(user):
    return retrieveLevel(user) == (4, 4)

def reduceLife(user):
    cur.execute('UPDATE Accounts SET lives=lives-1 WHERE user=%s', (user,))
    con.commit()

def terminateAccount(user):
    cur.execute('DELETE FROM Accounts WHERE user=%s', (user,))
    con.commit()

def task(user):
    L = retrieveLevel(user)
    A = False
    if L[1] == 1:
        A = guess_the_number(diff(L[0]))
    elif L[1] == 2:
        A = game_words(diff(L[0]))
    elif L[1] == 3:
        A = game_24()
    elif L[1] == 4:
        A = game_find_the_cats(diff(L[0]))

    if A:
        incrLevel(user)
    else:
        reduceLife(user)
        if lives(user) != 0:
            return task(user)
        else:
            return False

print(r'''
  ____      _                                _                  
 / ___|   _| |__   ___ _ ____   _____ _ __ | |_ _   _ _ __ ___ 
| |  | | | | '_ \ / _ \ '__\ \ / / _ \ '_ \| __| | | | '__/ _ \
| |__| |_| | |_) |  __/ |   \ V /  __/ | | | |_| |_| | | |  __/
 \____\__, |_.__/ \___|_|    \_/ \___|_| |_|\__|\__,_|_|  \___|
      |___/                                                      
''')
print('Loading ...')
sleep(2)  # Waits 2 seconds

# Login/Create Account
print('''
Login - 'L'
Create Account - 'A'
''')
ch = input().strip().upper()
user = None

if ch == 'L':
    user = login()
else:
    add_account()

sleep(2)

diff = lambda level: level - 1
sub = {1: 'Number Guess', 2: 'Unjumble', 3: 'Game 24', 4: 'Catfinder'}

# Start of game
try:
    print('Your account has been hacked.\nComplete the game to save your account')
    sleep(1)
    print('You have 3 lives. Once you lose all of them, your account gets deleted.')
    while True:
        if not is_completed(user) and lives(user) != 0:
            level, sublevel = retrieveLevel(user)
            print(f'''
Level: {level}
Sub-Level: {sublevel}
Up next: {sub[sublevel]}
Play - P
Exit - E
''')
            inp = input().strip().upper()
            if inp == 'P':
                if task(user) == False:
                    terminateAccount(user)
                    print('GAME OVER')
                    break
            else:
                break
except Exception as e:
    print(e)

