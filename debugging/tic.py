#!/usr/bin/python3

def print_board(board):
    """Prints the current Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there is a winner on the Tic-Tac-Toe board."""
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

def check_draw(board):
    """Checks if the game is a draw (all spots filled)."""
    for row in board:
        if " " in row:
            return False  # There's still an empty spot
    return True  # No empty spots, it's a draw

def tic_tac_toe():
    """Main game loop for Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Get user input for row and column with input validation
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                # Check if the input is within the valid range
                if 0 <= row < 3 and 0 <= col < 3:
                    if board[row][col] == " ":
                        break
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid input. Please enter a row and column between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter a valid number for row and column.")

        # Update the board with the player's move
        board[row][col] = player
        
        # Check if the current player won
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
