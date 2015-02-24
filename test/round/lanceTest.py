from lance import TasteOfTheLance
from controller import Controller
import unittest

class TasteOfTheLanceTest(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()
        self.lance = TasteOfTheLance(self.controller)

    def test_determine_strike_modifier_no_movement_no_tactical_no_bruises(self):
        lance = self.lance
        p1 = self.controller.get_p1()
        lance.determine_strike_modifier(p1)
        self.assertEquals(0, p1.get_strike_modifier())

    def test_determine_strike_modifier_first_movement_bonus_no_tactical_no_bruises(self):
        lance = self.lance
        p1 = self.controller.get_p1()
        p1.move(13)
        lance.determine_strike_modifier(p1)
        self.assertEquals(1, p1.get_strike_modifier())

    def test_determine_strike_modifier_second_movement_no_tactical_no_bruises(self):
        lance = self.lance
        p1 = self.controller.get_p1()
        p1.move(16)
        lance.determine_strike_modifier(p1)
        self.assertEquals(2, p1.get_strike_modifier())

    def test_determine_strike_modifier_first_movement_bonus_with_tactical_no_bruises(self):
        lance = self.lance
        p1 = self.controller.get_p1()
        p1.move(13)
        lance.determine_strike_modifier(p1, 1)
        self.assertEquals(2, p1.get_strike_modifier())

    def test_determine_strike_modifier_first_movement_bonus_with_tactical_with_three_bruises(self):
        lance = self.lance
        p1 = self.controller.get_p1()
        p1.move(13)
        for i in range(3):
            p1.add_bruise()
        lance.determine_strike_modifier(p1, 1)
        self.assertEquals(0, p1.get_strike_modifier())