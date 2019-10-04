

import random


choices = {'rock': 1, 'paper': 2, 'scissors': 3}


running = True
while running:
    p1 = random.randint(1, 3)
    p2 = int(input("Please choose {'rock': 1, 'paper': 2, 'scissors': 3}: "))
    print('robot : ', p1)
    print('you : ', p2)
    if p1 == p2:
        print('Tie')
        break
    if p2 == 3 or p1 == 3:
        if p1 == 1:
            if not (p1 > p2):
                print('robot wins')
                break
            if not (p1 < p2):
                print('you win')
                break
    if p1 > p2:
        print('robot wins yay')
    if p2 > p1:
        print('you win')
