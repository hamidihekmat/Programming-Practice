'''
Two students challenge each other to a basketball shootout. They agree to limit the number of
attempts to 3 throws each. The game will be constructed in two sessions where the first student will
make all 3 attempts followed by the second student. The student who makes the most baskets (gets
the ball in the hoop) will be declared the winner. In the case of a tie, the game will be repeated until a
winner can be determined.
'''




def basket():
    p1_score = 0
    p2_score = 0
    n_throws = 0
    while True:
        if n_throws == 3:
            n_throws = 0
            break
        n_throws += 1
        shot = int(input("Player 1 take the shot: 1 = In, 2 = Miss "))
        if shot == 1:
            p1_score += 1
        else:
            p1_score = p1_score

    while True:
        if n_throws == 3:
            n_throws = 0
            break
        n_throws += 1
        shot = int(input("Plater 2 take the shot: 1 = In, 2 = Miss "))
        if shot == 1:
            p2_score += 1
        else:
            p2_score = p2_score
    if p1_score > p2_score:
        print('Player 1, won!')
    elif p2_score > p1_score:
        print('Player 2, won!')
    else:
        print('Tie')
basket()
