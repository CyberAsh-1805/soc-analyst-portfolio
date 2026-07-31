import random
secret=random.randint(1,20)
attempts =5

while attempts>0:
    guess=int(input("guess a number between 1 and 20"))
    if guess==secret:
        print("correct! you win!!")
        break
    elif guess<secret:
        print("Too low!")
    else:
        print("too high!")
    attempts -= 1
    if attempts==0:
        print("sorry,you are out of chances. The number was", secret)
