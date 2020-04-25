import unittest
from mastermind.game import Game
from mastermind.peg import Peg
from random import choices

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
  
  def test_ten_incorrect_guesses_is_loss(self):
    game_two = Game([Peg("Green"), Peg("Blue"), Peg("Pink"), Peg("Yellow")])
    for i in range(0, 10):
      result = game_two.make_guess([Peg("Green"), Peg("Green"), Peg("Green"), Peg("Green")])
    self.assertEqual("Loss, too many guesses", result)

  def test_fifteen_incorrect_guesses_is_loss(self):
    game = Game([Peg("Green"), Peg("Blue"), Peg("Pink"), Peg("Yellow")])
    incorrect_guess = [Peg("Green"), Peg("Green"), Peg("Green"), Peg("Green")]
    for i in range(0, 15):
      result = game.make_guess(incorrect_guess)
    self.assertEqual("Loss, too many guesses", result)

  def test_correct_answer_on_tenth_try_is_win(self):
    solution = [Peg("Green"), Peg("Blue"), Peg("Pink"), Peg("Yellow")]
    game = Game(solution)
    incorrect_guess = [Peg("Green"), Peg("Green"), Peg("Green"), Peg("Green")]
    for i in range(0, 9):
      result = game.make_guess(incorrect_guess)
    self.assertEqual("Win!!!", game.make_guess(solution))

  def test_correct_answer_fourth_try_wins(self):
    solution = [Peg("Green"), Peg("Blue"), Peg("Pink"), Peg("Yellow")]
    game = Game(solution)
    incorrect_guess = [Peg("Green"), Peg("Green"), Peg("Green"), Peg("Green")]
    for i in range(0, 3):
      result = game.make_guess(incorrect_guess)
    self.assertEqual("Win!!!", game.make_guess(solution))

unittest.main()