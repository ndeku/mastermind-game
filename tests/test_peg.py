import unittest
from mastermind.peg import Peg

class peg_test(unittest.TestCase):
  "Unit Tests for Peg class value object"

  def test_peg_equals_itself(self):
    peg_a = Peg("Green")
    self.assertEqual(peg_a, peg_a, msg="Peg does not Equal itself")
    peg_a = Peg(1)
    self.assertEqual(peg_a, peg_a, msg="Peg does not Equal itself")

unittest.main()