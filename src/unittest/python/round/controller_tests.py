import unittest

from mockito import when, mock, unstub

from jousting.round.controller import Controller
from jousting.round.charge import Charge
from jousting.player.knight import Knight
from jousting.util import rps
import sys
from StringIO import StringIO


class TasteOfTheLanceTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Knight("P1")
        self.p2 = Knight("P2")

        self.controller = Controller(self.p1, self.p2)
        self.charge = Charge(self.controller)
        when(self.controller).get_p1().thenReturn(self.p1)
        when(self.controller).get_p2().thenReturn(self.p2)

        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        unstub()

    def test_round_p1_unhorsed(self):
        when(self.p1).get_unhorsed().thenReturn(True)

        self.controller.get_round_results(1)
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P2 wins by unhorsing Sir P1", output)

    def test_round_p2_unhorsed(self):
        when(self.p2).get_unhorsed().thenReturn(True)

        self.controller.get_round_results(1)
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P1 wins by unhorsing Sir P2", output)

    def test_round_p1_disqualified(self):
        when(self.p1).get_disqualified().thenReturn(True)

        self.controller.get_round_results(1)
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P1 has failed to start twice and has been disqualified.", output)

    def test_round_p2_disqualified(self):
        when(self.p2).get_disqualified().thenReturn(True)

        self.controller.get_round_results(1)
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P2 has failed to start twice and has been disqualified.", output)

    def test_final_results_p1_wins_points(self):
        when(self.p1).get_points().thenReturn(5)
        when(self.p2).get_points().thenReturn(0)

        self.controller.get_final_results()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P1 wins 5 to 0", output)

    def test_final_results_p2_wins_points(self):
        when(self.p1).get_points().thenReturn(0)
        when(self.p2).get_points().thenReturn(5)

        self.controller.get_final_results()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P2 wins 5 to 0", output)

    def test_final_results_tie_points(self):
        when(self.p1).get_points().thenReturn(5)
        when(self.p2).get_points().thenReturn(5)

        self.controller.get_final_results()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P1 and Sir P2 tie with 5 points.", output)

    def test_round_p1_failed_to_start(self):
        self.p1.move(5)
        self.p2.move(10)
        self.p1.determine_failed_to_start()
        self.p2.determine_failed_to_start()
        self.assertNotEquals(0, self.p1.get_current_position())
        self.assertNotEquals(0, self.p2.get_current_position())

        self.controller.get_round_results(1)
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P1 failed to start and the round is over.", output)

    def test_round_p2_failed_to_start(self):
        self.p1.move(10)
        self.p2.move(5)
        self.p1.determine_failed_to_start()
        self.p2.determine_failed_to_start()
        self.assertNotEquals(0, self.p1.get_current_position())
        self.assertNotEquals(0, self.p2.get_current_position())

        self.controller.get_round_results(1)
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P2 failed to start and the round is over.", output)

    def test_round_points(self):
        when(self.p1).get_points().thenReturn(2)
        when(self.p2).get_points().thenReturn(3)
        self.controller.get_round_results(1)
        output = sys.stdout.getvalue().strip()
        self.assertEquals("At the end of round 1 Sir P1 has 2 points, and Sir P2 has 3 points.", output)

    def test_reset_players(self):
        self.p1.move(5)
        self.p2.move(8)
        self.p1.determine_failed_to_start()
        self.p2.determine_failed_to_start()
        self.assertNotEquals(0, self.p1.get_current_position())
        self.assertNotEquals(0, self.p2.get_current_position())
        self.assertTrue(self.p1.get_failed_to_start())
        self.assertFalse(self.p2.get_failed_to_start())

        self.controller.reset_players_for_new_round()
        self.assertEquals(0, self.p1.get_current_position())
        self.assertEquals(0, self.p2.get_current_position())
        self.assertFalse(self.p1.get_failed_to_start())
        self.assertFalse(self.p2.get_failed_to_start())

    def test_full_round(self):
        self.controller.do_kick()
        self.assertNotEquals(0, self.p1.get_current_position())
        self.assertNotEquals(0, self.p2.get_current_position())

        when(self.p1).get_failed_to_start().thenReturn(False)
        when(self.p2).get_failed_to_start().thenReturn(False)
        self.controller.do_charge()

        when(self.p1).get_tactical_card().thenReturn(rps.COUNTER)
        when(self.p2).get_tactical_card().thenReturn(rps.SHIELD)
        self.controller.do_tactics_rps()
        self.assertTrue(self.p1.get_won_rps())

        when(self.p1).get_accept_heavy_blows().thenReturn(False)
        when(self.p2).get_accept_heavy_blows().thenReturn(False)
        self.controller.do_taste_of_the_lance()
        self.assertFalse(self.p1.get_unhorsed())
        self.assertFalse(self.p2.get_unhorsed())