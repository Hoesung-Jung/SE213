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
guess_number()