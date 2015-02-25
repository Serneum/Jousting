import unittest

from jousting.round.controller import Controller
from jousting.player.knight import Knight
from jousting.round.tactics_rps import TacticsCardRPS
from jousting.util import rps
from mockito import mock, when


class TacticsCardRPSTest(unittest.TestCase):
    def test_rps_tie(self):
        controller = mock(Controller)
        tactics_rps = TacticsCardRPS(controller)

        p1 = Knight("Name")
        p2 = Knight("Name")
        when(controller).get_p1().thenReturn(p1)
        when(controller).get_p2().thenReturn(p2)

        when(p1).get_tactical_card().thenReturn(rps.SHIELD)
        when(p2).get_tactical_card().thenReturn(rps.SHIELD)

        tactics_rps.do_tactics_rps()
        self.assertTrue(p1.get_accept_heavy_blows())
        self.assertTrue(p2.get_accept_heavy_blows())

    def test_rps_p1_wins_with_shield(self):
        controller = mock(Controller)
        tactics_rps = TacticsCardRPS(controller)

        p1 = Knight("Name")
        p2 = Knight("Name")
        when(controller).get_p1().thenReturn(p1)
        when(controller).get_p2().thenReturn(p2)

        when(p1).get_tactical_card().thenReturn(rps.SHIELD)
        when(p2).get_tactical_card().thenReturn(rps.LUNGE)

        tactics_rps.do_tactics_rps()
        self.assertFalse(p1.get_accept_heavy_blows())
        self.assertTrue(p2.get_accept_heavy_blows())

    def test_rps_p2_wins_with_shield(self):
        controller = mock(Controller)
        tactics_rps = TacticsCardRPS(controller)

        p1 = Knight("Name")
        p2 = Knight("Name")
        when(controller).get_p1().thenReturn(p1)
        when(controller).get_p2().thenReturn(p2)

        when(p1).get_tactical_card().thenReturn(rps.LUNGE)
        when(p2).get_tactical_card().thenReturn(rps.SHIELD)

        tactics_rps.do_tactics_rps()
        self.assertTrue(p1.get_accept_heavy_blows())
        self.assertFalse(p2.get_accept_heavy_blows())

    def test_rps_p1_wins_not_shield(self):
        controller = mock(Controller)
        tactics_rps = TacticsCardRPS(controller)

        p1 = Knight("Name")
        p2 = Knight("Name")
        when(controller).get_p1().thenReturn(p1)
        when(controller).get_p2().thenReturn(p2)

        when(p1).get_tactical_card().thenReturn(rps.COUNTER)
        when(p2).get_tactical_card().thenReturn(rps.SHIELD)

        tactics_rps.do_tactics_rps()
        self.assertTrue(p1.get_accept_heavy_blows())
        self.assertTrue(p2.get_accept_heavy_blows())
        self.assertTrue(p1.get_won_rps())
        self.assertFalse(p2.get_won_rps())

    def test_rps_p1_wins_not_shield(self):
        controller = mock(Controller)
        tactics_rps = TacticsCardRPS(controller)

        p1 = Knight("Name")
        p2 = Knight("Name")
        when(controller).get_p1().thenReturn(p1)
        when(controller).get_p2().thenReturn(p2)

        when(p1).get_tactical_card().thenReturn(rps.COUNTER)
        when(p2).get_tactical_card().thenReturn(rps.LUNGE)

        tactics_rps.do_tactics_rps()
        self.assertTrue(p1.get_accept_heavy_blows())
        self.assertTrue(p2.get_accept_heavy_blows())
        self.assertFalse(p1.get_won_rps())
        self.assertTrue(p2.get_won_rps())