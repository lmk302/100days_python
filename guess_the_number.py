# import random
# number = random.randrange(1,101)

from random import randint

number = randint(1,100)



difficulty = input("easy(10)? hard(5)?")

if difficulty == "easy":
    tries = 10
elif difficulty == "hard":
    tries = 5


print(number)




for _ in range(tries):
    print(f"remaining time: {tries}")
    user_guess = int(input("guess a number: "))    
    if  number > user_guess:
        print("Too low")
    elif number < user_guess:
        print("Too high")
    elif number == user_guess:
        print("Yay")
        break
    tries -= 1

if tries == 0:
    print("Your lose")
else:
    print("You won")