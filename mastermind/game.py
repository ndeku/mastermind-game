from mastermind.peg import Peg
from random import choices

class Game(object):
  "Understands state of game and win/loss"

  def __init__(self, answer=None):
    self.k = 4 # number of classes
    self.num_spaces = 4 # number of places/ spaces
    self.answer = answer if answer else self.__generate_solution()
    self.guesses = []

  def make_guess(self, guess):
    self.guesses.append(guess)
    if len(self.guesses) > 10:
      return "Loss, too many guesses" #CodeMaster wins
    if (self.__is_solution(guess)):
      return "Win!!!"
    if len(self.guesses) == 10:
      return "Loss, too many guesses"
    return "Try again"

  def __is_solution(self, guess):
    return (guess == self.answer)

  def __generate_solution(self):
    "Generates a game solution among possible classes"
    #classes = list(Peg(i) for i in range(0, self.k))
    classes = [Peg("Green"), Peg("Blue"), Peg("Pink"), Peg("Yellow")]
    return choices(classes, k=self.num_spaces)