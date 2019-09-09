import random


secret = random.randrange(1, 101)
running = True
while running:
    guess = int(input("Make a guess: "))
    if guess == secret:
        print("You guessed it!")
        running = False
    elif guess > secret:
        print('Too high')
    else:
        print('Too low')
