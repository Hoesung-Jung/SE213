
class BaseballGame:
    def __init__(self, seed_num = None):
        import random
        random.seed(seed_num)
        first_num, second_num, third_num = random.randrange(10), random.randrange(10), random.randrange(10)
        while first_num == second_num or first_num == third_num or second_num == third_num:
            if first_num == second_num:
                second_num = random.randrange(10)
            if first_num == third_num:
                third_num = random.randrange(10)
            if second_num == third_num:
                third_num = random.randrange(10)
        self.num = [first_num, second_num, third_num]

    def input_check(self):
        input_num = input("What is your guess: ")
        user_num = input_num.split(',')
        for i in range(len(user_num)):
            user_num[i] = user_num[i].strip()
        # input number가 유효한 판별
        for i in range(len(user_num)):
            if user_num.count(user_num[i]) != 1:
                return
            if user_num[i].isdecimal() == False:
                return
        if  len(user_num) != 3:
            return
        for i in range(len(user_num)):
            user_num[i] = int(user_num[i])
        return user_num

    def check_count(self, usr):
        strike = 0
        ball = 0
        for i in range(3):
            if usr[i] in self.num:
                if usr[i] == self.num[i]:
                    strike += 1
                else:
                    ball += 1
        else:
            return "{0}S {1}B".format(strike,ball)

    def play(self):
        while True:
            usr = BaseballGame.input_check(self)
            if not usr:
                print("Your input is not valid.")
                continue
            else:
                result = self.check_count(usr)
            if result == "3S 0B":
                print("You got it!!")
                break
            else:
                print(result)

new_game = BaseballGame(0)
print(new_game.num)
new_game.play()
