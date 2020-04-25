import unittest
from mastermind.game import Game
from mastermind.peg import Peg

class game_test(unittest.TestCase):
  "Unit Tests for Mastermind game class"

  def test_correct_answer_wins(self):
    guess = [Peg("Green"), Peg("Green"), Peg("Green"), Peg("Green")]
    self.assertEqual("Win!!!", Game().make_guess(guess))

  def test_incorrect_answer_does_not_win(self):
    guess = [Peg("Green"), Peg("Green"), Peg("Blue"), Peg("Blue")]
    self.assertNotEqual("Win!!!", Game().make_guess(guess))

unittest.main()