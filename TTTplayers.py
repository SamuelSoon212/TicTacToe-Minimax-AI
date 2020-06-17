import math, random

class HumanPlayer:
  def __init__(self, letter):
    self.letter = letter
  
  def get_move(self, game):
    while True:
      move = input(f"{self.letter}'s turn. Enter move from 0-8: ")
      try:
        move = int(move)
        if move not in game.available_moves():
          raise ValueError
        return move
      except ValueError:
        print("Invalid.")


class EasyBotPlayer:
  def __init__(self, letter):
    self.letter = letter
  
  def get_move(self, game):
    return random.choice(game.available_moves())


class HardBotPlayer:
  def __init__(self, letter):
    self.letter = letter

  def minimax(self, game, present_player):
    max_player = self.letter
    other_player = "X" if present_player == "O" else "O"
    if game.winner == other_player:
      if other_player == max_player:
        return {'position':None, 'score': 1 * (game.empty_squares_count() + 1)}
      else:
        return {'position':None, 'score': -1 * (game.empty_squares_count() + 1)}
    elif not game.empty_squares_check():
      return {'Postion':None, 'score':0}
    if present_player == max_player:
      best = {'postion':None, 'score':-math.inf}
    else:
      best = {'position':None, 'score':math.inf}
    for possible_move in game.available_moves():
      game.make_move(present_player, possible_move)
      simulation_score = self.minimax(game, other_player) # Recursion

      # Undo last move
      game.board[possible_move] = ' '
      game.winner = None
      simulation_score['position'] = possible_move
      if present_player == max_player:
        if simulation_score['score'] > best['score']:
          best = simulation_score
      else:
        if simulation_score['score'] < best['score']:
          best = simulation_score
    return best

  def get_move(self, game):
    if len(game.available_moves()) == 9:
      return random.choice(game.available_moves())
    else:
      return self.minimax(game, self.letter)['position']
  
