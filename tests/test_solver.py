import unittest
from mastermind.game import Game
from mastermind.peg import Peg
from mastermind.solver import RandomSolver
from scipy.stats import chisquare
import random

class solver_test(unittest.TestCase):
  "Unit Tests for Mastermind game class"

  def test_random_solver(self):
    game = Game()
    solver = RandomSolver(game)
    guesses = []
    for i in range(0, 50):
      guesses.append(solver.generate_guess())
    guesses = [str(g) for guess_list in guesses for g in guess_list]
    guess_map = {item: idx for idx, item in enumerate(set(guesses))}
    guesses = [guess_map.get(g) for g in guesses]
    t_stat, p_val = chisquare(guesses)
    self.assertGreater(p_val, 0.05, msg=f"p-value should should be < .05, pval={p_val}")

unittest.main()