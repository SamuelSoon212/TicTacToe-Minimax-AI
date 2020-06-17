import os, random
from TTTplayer import HumanPlayer, EasyBotPlayer, HardBotPlayer

class TTT:
  def __init__(self):
    self.board = self.make_board()
    self.winner = None

  @staticmethod
  def make_board():
    return [' ' for i in range(9)]

  def show_board(self):
    print(" _____ _____ _____ ")
    for row in [self.board[i*3 : i*3 + 3] for i in range(3)]:
      print("|     |     |     |")
      print("|  " + "  |  ".join(row) + "  |")
      print("|_____|_____|_____|")

  def empty_squares_check(self):
    return ' ' in self.board

  def empty_squares_count(self):
    return self.board.count(' ')

  def available_moves(self):
    return [i for i, x in enumerate(self.board) if x == ' ']

  def win_check(self, square, letter):
    row_index = square // 3
    row = self.board[row_index*3 : row_index*3 + 3]
    if all(c == letter for c in row):
      return True
    column_index = square % 3
    column = [self.board[i*3 + column_index] for i in range(3)]
    if all(c == letter for c in column):
      return True
    if square % 2 == 0:
      d1 = [self.board[i] for i in [0, 4, 8]]
      if all(c == letter for c in d1):
        return True
      d2 = [self.board[i] for i in [2, 4, 6]]
      if all(c == letter for c in d2):
        return True
    return False

  def make_move(self, player, move):
    try:
      self.board[move] = player.letter
      if self.win_check(move, player.letter):
        self.winner = player.letter
    except:
      self.board[move] = player
      if self.win_check(move, player):
        self.winner = player

def get_players():
  global player_1, player_2
  while True:
    print("Play against:")
    print("[1] Other Player")
    print("[2] Easy Bot")
    print("[3] Hard Bot\n")
    gamemode = input("Enter option: ")
    os.system('clear')
    try:
      gamemode = int(gamemode)
      if gamemode not in [1, 2, 3]:
        raise ValueError
      break
    except ValueError:
      print("Invalid")
  while True:
    print("What letter do you want to play as?")
    print("[1] X")
    print("[2] O\n")
    p1letter = input("Enter option: ")
    os.system('clear')
    try:
      p1letter = int(p1letter)
      if p1letter not in [1, 2]:
        raise ValueError
      break
    except ValueError:
      print("Invalid.")
  if p1letter == 1:
    p1letter = "X"
    p2letter = "O"
  else:
    p1letter = "O"
    p2letter = "X"
  if gamemode == 1:
    player_1 = HumanPlayer(p1letter)
    player_2 = HumanPlayer(p2letter)
  elif gamemode == 2:
    player_1 = HumanPlayer(p1letter)
    player_2 = EasyBotPlayer(p2letter)
  else:
    player_1 = HumanPlayer(p1letter)
    player_2 = HardBotPlayer(p2letter)

def PlayGame(game):
  get_players()
  game.make_board()
  first_player = random.choice([1,2])
  print(f"Player {first_player} goes first")
  for i in range(9):
    if game.winner != None:
      break
    game.show_board()
    if i % 2 == 0:
      current_player = player_1 if first_player == 1 else player_2
    else:
      current_player = player_2 if first_player == 1 else player_1
    player_move = current_player.get_move(game)
    os.system('clear')
    game.make_move(current_player, player_move)
    print(f"{current_player.letter} makes a move to square {player_move}")
  game.show_board()
  if game.winner == None:
    print("It's a tie!")
  else:
    print(f"{game.winner} has won!")

t = TTT()
PlayGame(t)
