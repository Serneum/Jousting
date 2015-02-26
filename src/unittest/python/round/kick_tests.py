import unittest

from mockito import mock, when, unstub

from jousting.round.kick import Kick
from jousting.round.controller import Controller
from jousting.player.knight import Knight


class KickTest(unittest.TestCase):
    def setUp(self):
        p1 = Knight("P1")
        p2 = Knight("P2")
        self.controller = Controller(p1, p2)
        self.kick = Kick(self.controller)

    def tearDown(self):
        unstub()

    def test_kick(self):
        self.kick.do_kick()
        self.assertNotEquals(self.kick._controller.get_p1(), self.kick._controller.get_p2())

    def test_knight_move_during_kick(self):
        for i in range(1000):
            self.kick.do_kick()
            self.assertNotEquals(0, self.kick._controller.get_p1().get_current_position())
            self.assertNotEquals(0, self.kick._controller.get_p2().get_current_position())

    def test_swap_logic(self):
        p1 = self.controller.get_p1()
        p2 = self.controller.get_p2()
        self.controller.set_p1(p2)
        self.controller.set_p2(p1)

        self.assertEquals(self.controller.get_p1(), p2)
        self.assertEquals(self.controller.get_p2(), p1)
        self.assertNotEquals(self.controller.get_p1(), self.controller.get_p2())