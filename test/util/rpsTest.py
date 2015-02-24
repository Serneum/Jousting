import rps
import unittest

class RPSTest(unittest.TestCase):

    def test_shield_vs_lunge(self):
        winner = rps.judge(rps.SHIELD, rps.LUNGE)
        self.assertEquals(1, winner)

        winner = rps.judge(rps.LUNGE, rps.SHIELD)
        self.assertEquals(2, winner)

    def test_lunge_vs_counter(self):
        winner = rps.judge(rps.LUNGE, rps.COUNTER)
        self.assertEquals(1, winner)

        winner = rps.judge(rps.COUNTER, rps.LUNGE)
        self.assertEquals(2, winner)

    def test_counter_vs_shield(self):
        winner = rps.judge(rps.COUNTER, rps.SHIELD)
        self.assertEquals(1, winner)

        winner = rps.judge(rps.SHIELD, rps.COUNTER)
        self.assertEquals(2, winner)

    def test_same_choice(self):
        winner = rps.judge(rps.SHIELD, rps.SHIELD)
        self.assertEquals(0, winner)

        winner = rps.judge(rps.LUNGE, rps.LUNGE)
        self.assertEquals(0, winner)

        winner = rps.judge(rps.COUNTER, rps.COUNTER)
        self.assertEquals(0, winner)