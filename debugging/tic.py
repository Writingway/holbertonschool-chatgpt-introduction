#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    while True:
        print_board(board)

        # Input validation loop
        while True:
            try:
                row = int(input(f"Enter row (0-2) for player {player}: "))
                col = int(input(f"Enter column (0-2) for player {player}: "))
            except ValueError:
                print("Invalid input! Please enter numbers 0, 1, or 2.")
                continue

            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    break
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Row and column must be between 0 and 2. Try again.")

        # Place the move
        board[row][col] = player
        moves += 1

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for a draw
        if moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
