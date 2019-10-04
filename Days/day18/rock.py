

import random


def game(p1, p2):
    running = True
    while running:
        print('robot : ', choices[p1])
        print('you : ', choices[p2])
        if p1 == p2:
            print('Tie')
            break
        if p2 == 3 or p1 == 3:
            if p1 == 1 or p2 == 1:
                if not (p1 > p2):
                    print('robot wins', choices[p1])
                    break
                if not (p1 < p2):
                    print('you win', choices[p2])
                    break
        if p1 > p2:
            print('robot wins yay', choices[p1])
            break
        if p2 > p1:
            print('you win', choices[p2])
            break


if __name__ == '__main__':
    choices = {1: 'rock', 2: 'paper', 3: 'scissors'}
    p1 = random.randint(1, 3)
    p2 = int(
        input("Please choose {'rock': 1, 'paper': 2, 'scissors': 3}: "))
    game(p1, p2)
