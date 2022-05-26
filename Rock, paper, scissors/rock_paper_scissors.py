import random

moves = ["rock", "paper", "scissors"]

win = "You Win!"
lose = "You lose."
draw = "Draw game."

computer_win = 0
player_win = 0
winner = False

print("Welcome to game: Win 3 round to win the game.")
print("Please choice your move: press R for rock, press P for paper, press S for scissor.")

while not winner:
    computer_move = (random.choice(moves))
    your_move = input("Your move: ")
    print(f"Computer move is: {computer_move}")

    if your_move == "r":
        print("Your move is: rock")
    elif your_move == "p":
        print("Your move is: paper")
    else:
        print("Your move is: scissors")
    print()

    if your_move == "r":
        if computer_move == "rock":
            print(draw)
        elif computer_move == "paper":
            print(lose)
            computer_win += 1
        else:
            print(win)
            player_win += 1
    elif your_move == "p":
        if computer_move == "paper":
            print(draw)
        elif computer_move == "rock":
            print(win)
            player_win += 1
        else:
            print(lose)
            computer_win += 1
    else:
        if computer_move == "scissors":
            print(draw)
        elif computer_move == "paper":
            print(win)
            player_win += 1
        else:
            print(lose)
            computer_win += 1

    print(f"Game result is Your win: {player_win}, computer win: {computer_win}.")
    print()
    if player_win == 3 or computer_win == 3:
        winner = True

if player_win == 3:
    print("\033[94mYou win the game!")
else:
    print("\033[93mYou lose the game.")
