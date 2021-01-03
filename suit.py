# Game Suit
import random

def play():
    user = input("Please Choose for 'r' = Rock, 'p' = Paper, 's' = scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'You win the game'

    return 'Sorry you lost'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())