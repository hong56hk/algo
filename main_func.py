# Switch turn between players
#  ie player 1 then 2 then back to 1 until the game end
# Keep the player within the board when he is moving
# ie the position of the player is always between 0 to 29 (why 0 and 29 not 1 and 30?)
# Gain computer chips when the player pass start point
# tips: if the position of the player is 0, something happens

# print welcome message
# 1. init games
# - board
# - players
# - game settings
# loop until game ends -> condition
#  2. ask user
#  3. do user action
#  4. switch players
# 5. print winner

import random




# Variables / Constants
BOARD_SIZE = 30
GAME_TURNS = 15
MAX_DICE_ROLL = 10


# Sample player object
# player = {
#   "name": "Player 1",
#   "position": 0,
# }
player_arr = [] # array of players
board = []
player_count = 2
current_player_turn = 0



# functions
def print_board():
  """
    print the board data
  """
  for i in range(0, BOARD_SIZE):
    ele = board[i]
    print(f"{i} {ele}", end="|")

def welcome():
  """
    Print welcome message and game rules
  """
  print("Welcome to the game")


def init_game():
  # create board
  for i in range(0, BOARD_SIZE):
    choice = random.choice(["blue", "green", "red"])
    board.append(choice)

  print_board()

  # create players
  user_input = input("How many players? ")
  player_count = int(user_input)
  print(f"Player count: {player_count}")

  for i in range(player_count):
    player = {
      "name": f"Player {i+1}",
      "position": 0,
    }
    player_arr.append(player)

  return board, player_arr, player_count



# main logic
def main():
  welcome()

  game_end = False
  board, player_arr, player_count = init_game()

  print("Game starts")

  while not game_end:
    # ask user input

    for i in range(player_count):
      _ = input(f"Player {current_player_turn+1} turn: Press Enter to roll dice")
      dice_result = random.randint(1, MAX_DICE_ROLL)
      print(f"Dice result: {dice_result}")



      current_player = player_arr[current_player_turn]
      current_player["position"] += dice_result

    # do user action

    # check if the player has reached the end
    # if yes, game ends
    pass

  # print winner






if __name__ == "__main__":
 main()
