import unittest
from mastermind.game import Game
from mastermind.peg import Peg

class game_test(unittest.TestCase):
  "Unit Tests for Mastermind game class"

  def test_correct_answer_wins(self):
    guess = [Peg("Green"), Peg("Green"), Peg("Green"), Peg("Green")]
    game = Game(guess)
    self.assertEqual("Win!!!", game.make_guess(guess))

  def test_incorrect_answer_does_not_win(self):
    game_one = Game([Peg("Green"), Peg("Green"), Peg("Blue"), Peg("Blue")])
    self.assertNotEqual("Win!!!", game_one.make_guess([Peg("Green"), Peg("Green"), Peg("Green"), Peg("Green")]))

  def test_generate_random_answer(self):
    game_two = Game() # game without solution
    guess = [Peg("Green"), Peg("Green"), Peg("Blue"), Peg("Blue")]
    self.assertNotEqual("Win!!!", game_two.make_guess(guess))

unittest.main()