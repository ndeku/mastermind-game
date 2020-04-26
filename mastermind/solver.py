from mastermind.peg import Peg
from mastermind.game import Game
from random import choices
from itertools import combinations

class Solver(object):
  "Understands how to generate guesses from a hint"

  def __init__(self, game):
    self.game = game

  def generate_guess(self):
    raiseNotDefined()

class RandomSolver(Solver):
  "Solver class which generates random guesses"

  def __init__(self, game):
    super(RandomSolver, self).__init__(game)

  def generate_guess(self, hint=None):
    "Generates a random code guess by sampling with replacement among possible classes"
    classes = [Peg("Green"), Peg("Blue"), Peg("Pink"), Peg("Yellow")]
    return choices(classes, k=self.game.num_spaces)