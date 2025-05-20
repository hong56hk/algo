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
total_turns = 0


# functions


# main logic
def main():
  print("Game settings")

  # create board
  for i in range(0, BOARD_SIZE):
    choice = random.choice(["blue", "green", "red"])
    board.append(choice)
    #print(f"{i} {choice}", end="|")
  board[random.randint(0, BOARD_SIZE)] = "shop"

  # create players
  user_input = input("How many players? ")
  player_count = int(user_input)
  print(f"Player count: {player_count}")


  for i in range(player_count):
    player = {
      "name": f"Player {i+1}",
      "position": 0,
      "computer_chip": 0,
    }
    player_arr.append(player)

  print("Game starts")
  for i in range(player_count):

    _ = input(f"Player {current_player_turn+1} turn: Press Enter to roll dice")
    dice_result = random.randint(1, MAX_DICE_ROLL)
    print(f"Dice result: {dice_result}")

    # do game logic
    current_player = player_arr[current_player_turn]

    new_position = current_player["position"] + dice_result
    new_position = new_position % BOARD_SIZE
    current_player["position"] = new_position

    # get board color of player new position
    color = board[new_position]
    if color == "blue":
      current_player["computer_chip"] += 3

    elif color == "green":
      # moving forward or back a couple of spaces
      movement = random.randint(-5, 5)
      new_position = new_position + movement
      new_position = new_position % BOARD_SIZE
      current_player["position"] = new_position

    elif color == "red":
      current_player["computer_chip"] -= 3
      if current_player["computer_chip"] < 0:
        current_player["computer_chip"] = 0
    elif color == "shop":
      print("You have reached the shop")
      print("You have", current_player["computer_chip"], "computer chips")
      user_input = input("Do you want to buy an extra dice with ?? computer? (y/n) ")
      pass
      # todo

    current_player_turn += 1
    current_player_turn = current_player_turn % player_count

    # check end game condition
    total_turns += 1
    if total_turns >= GAME_TURNS * player_count:
      break

  print("Game ends")



if __name__ == "__main__":
 main()


#
