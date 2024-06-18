def display_board(board):
    # Ensure each cell has a fixed width of 3 characters for alignment
    row1 = f" {board[1]:^3} | {board[2]:^3} | {board[3]:^3} "
    row2 = f" {board[4]:^3} | {board[5]:^3} | {board[6]:^3} "
    row3 = f" {board[7]:^3} | {board[8]:^3} | {board[9]:^3} "
    separator = "-" * 13  # Separator to visually separate rows
    print(row1)
    print(separator)
    print(row2)
    print(separator)
    print(row3)

# Initialize the board with 10 empty strings
test_board = [''] * 10

# Display the initial empty board
display_board(test_board)

# Function to get player input
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1 choose (X or O): ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Get player markers
player_1, player_2 = player_input()

# Function to place a marker on the board
def place_marker(board, marker, position):
    board[position] = marker
    return board

# Place a marker on the board (for example, 'X' at position 4)
updated_board = place_marker(test_board, 'X', 4)

# Display the updated board after placing the marker
display_board(updated_board)
