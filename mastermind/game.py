from mastermind.peg import Peg
from random import choices

class Game(object):
  "Understands state of game and win/loss"

  def __init__(self, answer=None):
    self.k = 4 # number of classes
    self.num_spaces = 4 # number of places/ spaces
    self.answer = answer if answer else self.__generate_solution(answer)

  def make_guess(self, guess):
    if (guess == self.answer):
      return "Win!!!"
    return "Try again"

  def __generate_solution(self, answer):
    "Generates a game solution among possible classes"
    classes = list(Peg(i) for i in range(0, self.k))
    return choices(classes, k=self.num_spaces)