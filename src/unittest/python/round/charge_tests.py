import unittest

from mockito import mock, when, unstub

from jousting.round.charge import Charge
from jousting.round.controller import Controller
from jousting.player.knight import Knight
from jousting.util import dice
import random


class TasteOfTheLanceTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Knight("P1")
        self.p2 = Knight("P2")
        controller = mock(Controller)
        self.charge = Charge(controller)

        when(controller).get_p1().thenReturn(self.p1)
        when(controller).get_p2().thenReturn(self.p2)

    def tearDown(self):
        unstub()

    def test_roll_movement(self):
        when(random).randint(1, dice.D6).thenReturn(5)
        roll_val = self.charge.roll_movement()
        self.assertEquals(5, roll_val)

    def test_roll_movement_negative(self):
        when(random).randint(1, dice.D6).thenReturn(-1)
        roll_val = self.charge.roll_movement()
        self.assertEquals(1, roll_val)

    def test_limit_movement_no_contact(self):
        when(self.p1).get_current_position().thenReturn(12)
        when(self.p2).get_current_position().thenReturn(5)
        spaces_to_move = self.charge.limit_movement(6)
        self.assertEquals(6, spaces_to_move)

    def test_limit_movement_with_contact(self):
        when(self.p1).get_current_position().thenReturn(12)
        when(self.p2).get_current_position().thenReturn(8)
        spaces_to_move = self.charge.limit_movement(6)
        self.assertEquals(4, spaces_to_move)

    def test_at_point_of_contact_true(self):
        when(self.p1).get_current_position().thenReturn(17)
        when(self.p2).get_current_position().thenReturn(7)
        at_contact = self.charge.check_point_of_contact()
        self.assertFalse(self.p1.get_failed_to_start())
        self.assertFalse(self.p2.get_failed_to_start())
        self.assertTrue(at_contact)

    def test_at_point_of_contact_false(self):
        when(self.p1).get_current_position().thenReturn(12)
        when(self.p2).get_current_position().thenReturn(8)
        at_contact = self.charge.check_point_of_contact()
        self.assertFalse(at_contact)

    def test_fail_start_p1(self):
        when(self.p1).get_current_position().thenReturn(6)
        when(self.p2).get_current_position().thenReturn(18)
        self.charge.do_charge()
        self.assertTrue(self.p1.get_failed_to_start())
        self.assertFalse(self.p2.get_failed_to_start())

    def test_fail_start_p2(self):
        when(self.p1).get_current_position().thenReturn(18)
        when(self.p2).get_current_position().thenReturn(6)
        self.charge.do_charge()
        self.assertFalse(self.p1.get_failed_to_start())
        self.assertTrue(self.p2.get_failed_to_start())

    def test_do_charge(self):
        when(random).randint(1, dice.D6).thenReturn(5)
        self.assertEquals(0, self.p1.get_current_position())
        self.assertEquals(0, self.p2.get_current_position())
        self.charge.do_charge()
        self.assertEquals(14, self.p1.get_current_position())
        self.assertEquals(10, self.p2.get_current_position())