# Simple Tic Tac Toe Game (2 Players)

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
    win_conditions = [
        [0, 1, 2],  # rows
        [3, 4, 5],  # rows
        [6, 7, 8],  # rows
        [0, 3, 6],  # col
        [1, 4, 7],  # col
        [2, 5, 8], ()]
    for condition in win_conditions:
        if player[condition[0]] == player[condition[1]] == player[condition[2]]:
            return True
        return False
