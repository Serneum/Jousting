import unittest

from mockito import mock, when, unstub

from jousting.round.lance import TasteOfTheLance
from jousting.round.controller import Controller
from jousting.player.knight import Knight
from jousting.util import dice
import random


class TasteOfTheLanceTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Knight("P1")
        self.p2 = Knight("P2")
        controller = mock(Controller)
        self.lance = TasteOfTheLance(controller)

        when(self.p1).get_current_position().thenReturn(0)
        when(self.p1).get_bruises().thenReturn(0)

        when(controller).get_p1().thenReturn(self.p1)
        when(controller).get_p2().thenReturn(self.p2)

    def tearDown(self):
        unstub()

    def test_determine_strike_modifier_no_movement_no_tactical_no_bruises(self):
        self.lance.determine_strike_modifier(self.p1)
        self.assertEquals(0, self.p1.get_strike_modifier())

    def test_determine_strike_modifier_first_movement_bonus_no_tactical_no_bruises(self):
        when(self.p1).get_current_position().thenReturn(13)
        self.lance.determine_strike_modifier(self.p1)
        self.assertEquals(1, self.p1.get_strike_modifier())

    def test_determine_strike_modifier_second_movement_no_tactical_no_bruises(self):
        when(self.p1).get_current_position().thenReturn(16)
        self.lance.determine_strike_modifier(self.p1)
        self.assertEquals(2, self.p1.get_strike_modifier())

    def test_determine_strike_modifier_first_movement_bonus_with_tactical_no_bruises(self):
        when(self.p1).get_current_position().thenReturn(13)
        self.lance.determine_strike_modifier(self.p1, 1)
        self.assertEquals(2, self.p1.get_strike_modifier())

    def test_determine_strike_modifier_first_movement_bonus_with_tactical_with_three_bruises(self):
        when(self.p1).get_current_position().thenReturn(13)
        when(self.p1).get_bruises().thenReturn(3)
        self.lance.determine_strike_modifier(self.p1, 1)
        self.assertEquals(0, self.p1.get_strike_modifier())

    def test_strike_roll_glancing(self):
        when(self.p1).get_strike_modifier().thenReturn(0)
        when(random).randint(1, dice.D6).thenReturn(1)
        self.lance.strike_roll(self.p1, self.p2)
        self.assertEquals(0, self.p1.get_points())

    def test_strike_roll_light(self):
        when(self.p1).get_strike_modifier().thenReturn(0)
        when(random).randint(1, dice.D6).thenReturn(3)
        self.lance.strike_roll(self.p1, self.p2)
        self.assertEquals(2, self.p1.get_points())

    def test_strike_roll_heavy(self):
        when(self.p1).get_strike_modifier().thenReturn(0)
        when(random).randint(1, dice.D6).thenReturn(5)
        self.lance.strike_roll(self.p1, self.p2)
        self.assertEquals(3, self.p1.get_points())

    def test_strike_roll_accept_heavy_false(self):
        when(self.p1).get_strike_modifier().thenReturn(0)
        when(self.p2).get_accept_heavy_blows().thenReturn(False)
        when(random).randint(1, dice.D6).thenReturn(5)
        self.lance.strike_roll(self.p1, self.p2)
        self.assertEquals(2, self.p1.get_points())

    def test_heavy_blow_roll_add_bruise(self):
        when(random).randint(1, dice.D6).thenReturn(4)
        self.assertEquals(0, self.p2.get_bruises())
        self.lance.heavy_blow_roll(self.p2)
        self.assertEquals(1, self.p2.get_bruises())

    def test_heavy_blow_roll_unhorse(self):
        when(random).randint(1, dice.D6).thenReturn(6)
        self.lance.heavy_blow_roll(self.p2)
        self.assertTrue(self.p2.get_unhorsed())

    def test_lance_break_roll_no_break(self):
        when(random).randint(1, dice.D6).thenReturn(3)
        self.assertEquals(0, self.p1.get_points())
        self.lance.lance_break_roll(self.p1)
        self.assertEquals(0, self.p1.get_points())

    def test_lance_break_roll_break(self):
        when(random).randint(1, dice.D6).thenReturn(4)
        self.assertEquals(0, self.p1.get_points())
        self.lance.lance_break_roll(self.p1)
        self.assertEquals(1, self.p1.get_points())

    def test_do_taste_of_the_lance(self):
        when(random).randint(1, dice.D6).thenReturn(4)
        self.assertEquals(0, self.p1.get_points())
        self.assertEquals(0, self.p2.get_points())
        self.lance.do_taste_of_the_lance()
        self.assertEquals(2, self.p1.get_points())
        self.assertEquals(2, self.p2.get_points())