#!/usr/bin/python3

def print_board(board):
    """Prints the current state of the Tic Tac Toe board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Avoid printing separator after the last row
            print("-" * 5)

def check_winner(board):
    """Checks if there is a winner in the current board state."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_tie(board):
    """Checks if the board is full and no winner is found (tie)."""
    for row in board:
        if " " in row:  # If there's an empty spot, it's not a tie
            return False
    return True

def tic_tac_toe():
    """Runs the main game loop for Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        
        # Get valid row input
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row not in [0, 1, 2]:
                    print("Invalid input! Please enter a row number between 0 and 2.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a numeric value for the row.")
                continue

            # Get valid column input
            while True:
                try:
                    col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                    if col not in [0, 1, 2]:
                        print("Invalid input! Please enter a column number between 0 and 2.")
                        continue
                except ValueError:
                    print("Invalid input! Please enter a numeric value for the column.")
                    continue

                # Check if the spot is empty
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("That spot is already taken! Try again.")
                    continue

            break
        
        # Check for a winner or tie after each move
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()