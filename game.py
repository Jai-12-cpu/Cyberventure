from random import choice
from time import sleep


def game_24_check_operation(oper):
    allowed = "1234567890+-*/() "
    is_number = False

    for i in oper:
        if i not in allowed:
            return False
        try:
            int(i)
            if is_number:
                return False  # prevent number concatenation
            is_number = True
        except ValueError:
            is_number = False

    return True


def game_24():
    all_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    choices = []

    for _ in range(4):
        ch = choice(all_choices)
        all_choices.remove(ch)
        choices.append(ch)

    # Unsolvable cases
    if set(choices) in [{1, 6, 7, 8}, {3, 4, 6, 7}]:
        choices = [1, 2, 3, 4]

    print(r"""
  ____  _  _      ____                       
 |___ \| || |    / ___| __ _ _ __ ___   ___  
   __) | || |_  | |  _ / _` | '_ ` _ \ / _ \ 
  / __/|__   _| | |_| | (_| | | | | | |  __/ 
 |_____|  |_|    \____|\__,_|_| |_| |_|\___| 
""")

    print("Do math operations to get the number 24!")

    while True:
        print(f"Your choices are: {choices}")

        operations = input(
            "Enter your numbers along with operations (+, -, *, /)\n"
            "(brackets are allowed): "
        )

        included_number_count = 0
        for i in choices:
            if str(i) in operations:
                included_number_count += 1

        if included_number_count != 4:
            print("Please use all 4 numbers!")
            continue

        if not game_24_check_operation(operations):
            print("Please only use allowed operations!")
            continue

        try:
            result = eval(operations)
            result = int(result)
        except Exception:
            print("Don't type gibberish!")
            continue

        if result == 24:
            print(f"You won! {operations} = {result}")
            return True
        else:
            print(f"You lose! {operations} = {result}, better luck next time!")
            return False
