from dice import D3, roll
from phase import Phase

class Kick(Phase):

    def do_kick(self):
        p1 = self.controller.get_p1()
        p2 = self.controller.get_p2()

        # We only move during the initial roll
        p1_roll = roll(D3)
        p1.move(p1_roll)

        p2_roll = roll(D3)
        p2.move(p2_roll)

        # Roll until we know who will move first in the Charge phase
        while p1_roll == p2_roll:
            p1_roll = roll(D3)
            p2_roll = roll(D3)

        # A round will start with the first player in the p1 spot, so we only need to swap
        # when the first player goes second
        if p1_roll < p2_roll:
            self.controller.set_p1(p2)
            self.controller.set_p2(p1)