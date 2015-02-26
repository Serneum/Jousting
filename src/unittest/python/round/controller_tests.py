import unittest

from mockito import when, unstub

from jousting.round.controller import Controller
from jousting.round.charge import Charge
from jousting.player.knight import Knight
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

        # Set both players to not accept heavy blows to avoid unhorsing unless that is what we are testing
        when(self.p1).get_accept_heavy_blows().thenReturn(False)
        when(self.p2).get_accept_heavy_blows().thenReturn(False)

        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        unstub()

    def test_do_game_p1_unhorsed(self):
        when(self.p1).get_failed_to_start().thenReturn(False)
        when(self.p2).get_failed_to_start().thenReturn(False)
        when(self.p1).get_unhorsed().thenReturn(True)

        self.controller.do_game()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P2 wins by unhorsing Sir P1", output)

    def test_do_game_p2_unhorsed(self):
        when(self.p1).get_failed_to_start().thenReturn(False)
        when(self.p2).get_failed_to_start().thenReturn(False)
        when(self.p2).get_unhorsed().thenReturn(True)

        self.controller.do_game()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P1 wins by unhorsing Sir P2", output)

    def test_do_game_p1_disqualified(self):
        when(self.p1).get_failed_to_start().thenReturn(False)
        when(self.p2).get_failed_to_start().thenReturn(False)
        when(self.p1).get_disqualified().thenReturn(True)

        self.controller.do_game()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P1 has failed to start twice and has been disqualified.", output)

    def test_do_game_p2_disqualified(self):
        when(self.p1).get_failed_to_start().thenReturn(False)
        when(self.p2).get_failed_to_start().thenReturn(False)
        when(self.p2).get_disqualified().thenReturn(True)

        self.controller.do_game()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P2 has failed to start twice and has been disqualified.", output)

    def test_do_game_p1_wins_points(self):
        when(self.p1).get_failed_to_start().thenReturn(False)
        when(self.p2).get_failed_to_start().thenReturn(False)
        when(self.p1).get_points().thenReturn(5)
        when(self.p2).get_points().thenReturn(0)

        self.controller.do_game()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("\n".join(["At the end of round 1 Sir P1 has 5 points, and Sir P2 has 0 points.",
                                     "At the end of round 2 Sir P1 has 5 points, and Sir P2 has 0 points.",
                                     "At the end of round 3 Sir P1 has 5 points, and Sir P2 has 0 points.",
                                     "Sir P1 wins 5 to 0"]), output)

    def test_do_game_p2_wins_points(self):
        when(self.p1).get_failed_to_start().thenReturn(False)
        when(self.p2).get_failed_to_start().thenReturn(False)
        when(self.p1).get_points().thenReturn(0)
        when(self.p2).get_points().thenReturn(5)

        self.controller.do_game()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("\n".join(["At the end of round 1 Sir P1 has 0 points, and Sir P2 has 5 points.",
                                     "At the end of round 2 Sir P1 has 0 points, and Sir P2 has 5 points.",
                                     "At the end of round 3 Sir P1 has 0 points, and Sir P2 has 5 points.",
                                     "Sir P2 wins 5 to 0"]), output)

    def test_do_game_tie_points(self):
        when(self.p1).get_failed_to_start().thenReturn(False)
        when(self.p2).get_failed_to_start().thenReturn(False)
        when(self.p1).get_points().thenReturn(5)
        when(self.p2).get_points().thenReturn(5)

        self.controller.do_game()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("\n".join(["At the end of round 1 Sir P1 has 5 points, and Sir P2 has 5 points.",
                                     "At the end of round 2 Sir P1 has 5 points, and Sir P2 has 5 points.",
                                     "At the end of round 3 Sir P1 has 5 points, and Sir P2 has 5 points.",
                                     "Sir P1 and Sir P2 tie with 5 points."]), output)

    def test_do_round_p1_failed_to_start(self):
        self.p1.move(5)
        self.p2.move(10)
        self.p1.determine_failed_to_start()
        self.p2.determine_failed_to_start()
        self.assertNotEquals(0, self.p1.get_current_position())
        self.assertNotEquals(0, self.p2.get_current_position())

        self.controller.do_round()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P1 failed to start and the round is over.", output)

    def test_do_round_p2_failed_to_start(self):
        self.p1.move(10)
        self.p2.move(5)
        self.p1.determine_failed_to_start()
        self.p2.determine_failed_to_start()
        self.assertNotEquals(0, self.p1.get_current_position())
        self.assertNotEquals(0, self.p2.get_current_position())

        self.controller.do_round()
        output = sys.stdout.getvalue().strip()
        self.assertEquals("Sir P2 failed to start and the round is over.", output)

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