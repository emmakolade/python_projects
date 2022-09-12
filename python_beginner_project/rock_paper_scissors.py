import random

def play_game():
    user = input("choose one out of the three: 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it is a tie'

    if who_won(user, computer):
        return "You won"

    return "You Lost"

def who_won(player, comp):
    # using this condition : r > p, p > s, s > r
    # return true if player wins
    if (player == 'r' and comp == 'p') or (player == 'p' and comp == 's') or (player == 's' and comp == 'r'):
        return True

print(play_game())