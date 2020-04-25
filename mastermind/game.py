from mastermind.peg import Peg
#from peg import Peg

class Game(object):
  "Understands state of game and win/loss"

  def __init__(self):
    self.answer = [Peg("Green"), Peg("Green"), Peg("Green"), Peg("Green")]

  def make_guess(self, guess):
    if (guess == self.answer):
      return "Win!!!"
    return "Try again"