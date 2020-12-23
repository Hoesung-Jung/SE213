import random

def guess_number(seed_num=None):
    random.seed(seed_num)
    real_num = random.randint(0,99)
    guess = int(input("Enter your guess: "))
    while guess != real_num:
        if guess < real_num:
            print("Too small!")
            guess = int(input("Enter your guess: "))
        elif guess > real_num:
            print("Too big!")
            guess = int(input("Enter your guess: "))

    print("You got it!")


guess_number()


#mine
import random


def guess_number(seed_num=None):
    random.seed(seed_num)
    sol_num = random.randrange(1, 100)
    user_num1 = input("Enter your guess: ")
    while user_num1.isdecimal() == False:
        user_num1 = input("Enter your guess: ")
    user_num = int(user_num1)
    if user_num > sol_num:
        print("Too big!")
    elif user_num < sol_num:
        print("Too small!")
    elif user_num == sol_num:
        print("You got it!")
    while sol_num != user_num:
        user_num1 = input("Enter your guess: ")
        while user_num1.isdecimal() == False:
            user_num1 = input("Enter your guess: ")
        user_num = int(user_num1)
        if user_num > sol_num:
            print("Too big!")
        elif user_num < sol_num:
            print("Too small!")
        elif user_num == sol_num:
            print("You got it!")


# 민서
import random

def guess_number(seed_num=None):
    """Generate a random and tell user whether their guessed number is correct"""
    """ seed_num으로 seed값을 고정 후 진행 """
    random.seed(seed_num)
    b=random.randrange(0,100)
    while True:
        p=input('Enter your guess:')
        a=int(p)
        if a==b:
            print("You got it!")
            break
        elif a>b:
            print("Too big!")
        else:
            print("Too small")
    return None
