import dice
import unittest

class DiceTest(unittest.TestCase):

    def testSingleDie(self):
        for x in range(10000):
            val = dice.roll(dice.D6)
            self.assertTrue(0 < val <= 6)

    def testMultipleDie(self):
        for x in range(10000):
            val = dice.roll(dice.D6, 10, 0)
            self.assertTrue(10 < val <= 60)

    def testPositiveModifier(self):
        for x in range(10000):
            val = dice.roll(dice.D6, 10, 5)
            self.assertTrue(15 < val <= 65)

    def testNegativeModifier(self):
        for x in range(10000):
            val = dice.roll(dice.D6, 10, -5)
            self.assertTrue(5 < val <= 55)