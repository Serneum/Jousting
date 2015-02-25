from knight import Knight
from rps import SHIELD
import unittest

class KnightTest(unittest.TestCase):

    def setUp(self):
        self.knight = Knight("Lancelot")

    def test_move(self):
        knight = self.knight
        self.assertEquals(0, knight.get_current_position())

        knight.move(5)
        self.assertEquals(5, knight.get_current_position())

    def test_bruises(self):
        knight = self.knight
        self.assertEquals(0, knight.get_bruises())

        knight.add_bruise()
        self.assertEquals(1, knight.get_bruises())

    def test_tactical_card(self):
        knight = self.knight
        self.assertEquals(-1, knight.get_tactical_card())

        knight.set_tactical_card(SHIELD)
        self.assertEquals(0, knight.get_tactical_card())

    def test_accept_heavy_blows(self):
        knight = self.knight
        self.assertTrue(knight.get_accept_heavy_blows())

        knight.set_accept_heavy_blows(False)
        self.assertFalse(knight.get_accept_heavy_blows())

    def test_disqualification(self):
        knight = self.knight
        self.assertFalse(knight.get_disqualified())

        knight.add_fail_start()
        self.assertFalse(knight.get_disqualified())

        knight.add_fail_start()
        self.assertTrue(knight.get_disqualified())

    def test_points(self):
        knight = self.knight
        self.assertEquals(0, knight.get_points())

        knight.add_points(5)
        self.assertEquals(5, knight.get_points())

    def test_unhorsed(self):
        knight = self.knight
        self.assertFalse(knight.get_unhorsed())

        knight.set_unhorsed(True)
        self.assertTrue(knight.get_unhorsed())

    def test_strike_modifier(self):
        knight = self.knight
        self.assertEquals(0, knight.get_strike_modifier())

        knight.set_strike_modifier(5)
        self.assertEquals(5, knight.get_strike_modifier())

    def test_failure_to_start(self):
        knight = self.knight
        self.assertTrue(knight.get_failed_to_start())

        knight.move(6)
        self.assertTrue(knight.get_failed_to_start())

        knight.reset_for_round()
        knight.move(7)
        self.assertFalse(knight.get_failed_to_start())
