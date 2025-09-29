import random

class fruitQuiz:
    def __init__(self):
        self.fruits={'apple':'red',
					'orange':'orange',
					'watermelon':'green',
					'banana':'yellow'}
    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruits.items()))

            print(f"What is the color of {fruit}?")
            user_ans = input()

            if(user_ans.lower() == color):
                print("Correct answer!")
            else:
                print("wrong!")
            option = int(input("enter 0 , if you want to play again otherwise enter 1: "))
            if(option):
                break

print("Welcome to fruit quiz")
fq = fruitQuiz()
fq.quiz()
