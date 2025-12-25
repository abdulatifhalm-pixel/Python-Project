# Tic Tac Toe Game (Two Players)

board = [' ' for _ in range(9)]


def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(player):
    win_conditions = [[0, 1, 2], [3, 4, 5], ]
