from mastermind.peg import Peg
from random import choices

class Game(object):
  "Understands state of game and win/loss"

  def __init__(self, solution=None):
    self.classes = [Peg("Green"), Peg("Blue"), Peg("Pink"), Peg("Yellow")]
    self.hints = [Peg("Black"), Peg("White")]
    self.num_spaces = 4 # number of places/ spaces
    self.solution = solution if solution else self.__generate_solution()
    self.guesses = []

  def make_guess(self, guess):
    self.guesses.append(guess)
    if ((self.__is_solution(guess)) & (len(self.guesses) <= 10)):
      return "Win!!!", "" # CodeBreaker wins
    if (len(self.guesses) >= 10):
      return "Loss, too many guesses", "" #CodeMaster wins
    return "Try again", self.get_hint(guess)

  def __is_solution(self, guess):
    return (guess == self.solution)

  def __generate_solution(self):
    "Generates a game solution among possible classes"
    return choices(self.classes, k=self.num_spaces)

  def get_classes(self):
    return self.classes

  def get_hint(self, guess):
    "Return keypegs as hint"
    hint = []
    for i, item in enumerate(guess):
      if item == self.solution[i]:
        hint.append(self.hints[0]) # correct in both color and position
        continue
      if guess.count(item) > self.solution.count(item):
        hint.append(None) # no hint if count of item exceeds occurances in solution 
        continue
      if item in self.solution:
        hint.append(self.hints[1]) # correct color code peg placed in the wrong position
        continue
      hint.append(None)
    return hint