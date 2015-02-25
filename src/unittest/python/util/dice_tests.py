import unittest

from jousting.util import dice


class DiceTest(unittest.TestCase):

    def test_single_die(self):
        for x in range(10000):
            val = dice.roll(dice.D6)
            self.assertTrue(0 < val <= 6)

    def test_multiple_die(self):
        for x in range(10000):
            val = dice.roll(dice.D6, 10, 0)
            self.assertTrue(10 < val <= 60)

    def test_positive_modifier(self):
        for x in range(10000):
            val = dice.roll(dice.D6, 10, 5)
            self.assertTrue(15 < val <= 65)

    def test_negative_modifier(self):
        for x in range(10000):
            val = dice.roll(dice.D6, 10, -5)
            self.assertTrue(5 < val <= 55)