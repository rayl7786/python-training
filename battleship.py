from random import randint

# Initial board
board = []

# Allow player to create size of board
print "What size do you want the board to be? "

# Check to see if any input when entering board dimensions
def row_length():
  while True:
    try:
      length_of_row = int(raw_input("Column Row: "))
      return length_of_row
      break
    except ValueError:
      print( "" )
      print( " +++ You need to enter a number. +++ " )
      print( "" )

def col_length():
  while True:
    try:
      length_of_column = int(raw_input("Column Length: "))
      return length_of_column
      break
    except ValueError:
      print( "" )
      print( " +++ You need to enter a number. +++ " )
      print( "" )

length_of_row = row_length()
length_of_column = int(col_length())

# Create Board
for x in range(0, length_of_column):
  board.append(["O"] * length_of_row)

def print_board(board):
  for row in board:
    print "  ".join(row)

# Display Board
print( "===" * length_of_column )
print_board(board)
print( "==="  * length_of_column )

# Functions to create random coordinates for ship(s)
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

# Decide number of ships depending on size of board
def create_ships():
  number_of_spaces = length_of_row * length_of_column
  number_of_ships = 1
  while number_of_spaces > 25:
    number_of_spaces = number_of_spaces - 25
    number_of_ships += 1
  return number_of_ships

number_of_ships = create_ships()

# Create ship coordinates
def create_ship_coordinates():
  coor = {}
  for x in range(1, (number_of_ships + 1)):
    ship_row = random_row(board)
    ship_col = random_col(board)
    coor["ship {0}".format(x)] = "(" + str(ship_row) + ", " + str(ship_col) + ")"
  return coor

ship_coordinates = create_ship_coordinates()

# How many guesses depends on the number of ships (4 guesses for every 1 ship)
number_of_guesses = number_of_ships * 4

# Main part of game
while number_of_guesses > 0:
  if len(ship_coordinates) == 0:
    print( " ++**++** !! You WON !! ++**++** " )
    break
  print( "" )
  print( "Number of ships: " + str(number_of_ships) + " left" )
  print( "You have " + str(number_of_guesses) + " guesses left." )
  print( "" )
  while True:
    try:
      guess_row = int(raw_input("Guess Row: ")) - 1
      break
    except ValueError:
      print( "" )
      print( " +++ You need to enter a number. +++ " )
      print( "" )
  while True:
    try:
      guess_col = int(raw_input("Guess Column: ")) - 1
      break
    except ValueError:
      print( "" )
      print( " +++ You need to enter a number. +++ " )
      print( "" )
  guess_coordinates = guess_row, guess_col
  for key, value in ship_coordinates.items():
    if str(guess_coordinates) in value:
      print( " ***** Congratulations! You sank " + key + " battleship! ***** " )
      del ship_coordinates[key]
      board[guess_row][guess_col] = "!"
      number_of_ships -= 1
      number_of_guesses -= 1
      break
  else:
    if guess_row not in range(length_of_row) or guess_col not in range(length_of_column):
      print( " +++ Oops, that's not even in the ocean. +++ " )
      raw_input("Press ENTER To Continue")
    elif board[guess_row][guess_col] == "X":
      print( " +++ You guessed that one already. +++ " )
      raw_input("Press ENTER To Continue")
    elif board[guess_row][guess_col] == "!":
      print( " +++ That is where you sank a ship already!. +++ " )
      raw_input("Press ENTER To Continue")
    else:
      print( " +++ You missed my battleship! +++ " )
      board[guess_row][guess_col] = "X"
      number_of_guesses -= 1
  if number_of_guesses == 0:
    print( "+++++++++" )
    print( "Game Over" )
    print( "+++++++++" )
  else:
    print( "" )
    print_board(board)
    print( "" )
