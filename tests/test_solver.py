import unittest
from mastermind.game import Game
from mastermind.peg import Peg
from mastermind.solver import RandomSolver
from scipy.stats import chisquare

class solver_test(unittest.TestCase):
  "Unit Tests for Mastermind game class"

  def test_random_solver(self):
    game = Game()
    solver = RandomSolver(game)
    guesses = []
    for i in range(0, 50):
      guesses.append(solver.generate_guess())
    guesses = [hash(g) for guess_list in guesses for g in guess_list]
    t_stat, p_val = chisquare(guesses)
    self.assertGreater(p_val, .1)

unittest.main()