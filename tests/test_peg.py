import unittest
from mastermind.peg import Peg

class peg_test(unittest.TestCase):
  "Unit Tests for Peg class value object"

  def test_peg_equals_itself(self):
    peg_a = Peg("Green")
    self.assertEqual(peg_a, peg_a, msg="Peg does not Equal itself")
    peg_a = Peg(1)
    self.assertEqual(peg_a, peg_a, msg="Peg does not Equal itself")

  def test_two_green_pegs_equal(self):
    peg_a = Peg("Green")
    peg_b = Peg("Green")
    self.assertEqual(peg_a, peg_b, msg=f"Two Green Pegs should be equal: {peg_a} {peg_b}")

  def test_pegs_different_color_not_equal(self):
    peg_a = Peg("Green")
    peg_b = Peg("Blue")
    self.assertNotEqual(peg_a, peg_b, msg=f"Two Pegs of different color should be equal: {peg_a} {peg_b}")

  def test_peg_string_representation_is_readable(self):
    peg_a = Peg("Green")
    self.assertEqual("Green", str(peg_a))
    self.assertEqual("Blue", str(Peg("Blue")))

unittest.main()