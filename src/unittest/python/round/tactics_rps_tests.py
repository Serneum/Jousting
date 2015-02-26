import unittest

from jousting.round.controller import Controller
from jousting.player.knight import Knight
from jousting.round.tactics_rps import TacticsCardRPS
from jousting.util import rps
from mockito import mock, when, unstub


class TacticsCardRPSTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Knight("P1")
        self.p2 = Knight("P2")
        controller = mock(Controller)
        self.tactics_rps = TacticsCardRPS(controller)

        when(controller).get_p1().thenReturn(self.p1)
        when(controller).get_p2().thenReturn(self.p2)

    def tearDown(self):
        unstub()

    def test_rps_tie(self):
        when(self.p1).get_tactical_card().thenReturn(rps.SHIELD)
        when(self.p2).get_tactical_card().thenReturn(rps.SHIELD)

        self.tactics_rps.do_tactics_rps()
        self.assertTrue(self.p1.get_accept_heavy_blows())
        self.assertTrue(self.p2.get_accept_heavy_blows())

    def test_rps_p1_wins_with_shield(self):
        when(self.p1).get_tactical_card().thenReturn(rps.SHIELD)
        when(self.p2).get_tactical_card().thenReturn(rps.LUNGE)

        self.tactics_rps.do_tactics_rps()
        self.assertFalse(self.p1.get_accept_heavy_blows())
        self.assertTrue(self.p2.get_accept_heavy_blows())

    def test_rps_p2_wins_with_shield(self):
        when(self.p1).get_tactical_card().thenReturn(rps.LUNGE)
        when(self.p2).get_tactical_card().thenReturn(rps.SHIELD)

        self.tactics_rps.do_tactics_rps()
        self.assertTrue(self.p1.get_accept_heavy_blows())
        self.assertFalse(self.p2.get_accept_heavy_blows())

    def test_rps_p1_wins_not_shield(self):
        when(self.p1).get_tactical_card().thenReturn(rps.COUNTER)
        when(self.p2).get_tactical_card().thenReturn(rps.SHIELD)

        self.tactics_rps.do_tactics_rps()
        self.assertTrue(self.p1.get_accept_heavy_blows())
        self.assertTrue(self.p2.get_accept_heavy_blows())
        self.assertTrue(self.p1.get_won_rps())
        self.assertFalse(self.p2.get_won_rps())

    def test_rps_p2_wins_not_shield(self):
        when(self.p1).get_tactical_card().thenReturn(rps.COUNTER)
        when(self.p2).get_tactical_card().thenReturn(rps.LUNGE)

        self.tactics_rps.do_tactics_rps()
        self.assertTrue(self.p1.get_accept_heavy_blows())
        self.assertTrue(self.p2.get_accept_heavy_blows())
        self.assertFalse(self.p1.get_won_rps())
        self.assertTrue(self.p2.get_won_rps())