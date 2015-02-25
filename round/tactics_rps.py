from phase import Phase
import rps

class TacticsCardRPS(Phase):
    def do_tactics_rps(self):
        p1 = self._controller.get_p1()
        p2 = self._controller.get_p2()
        p1_card = p1.get_tactical_card()
        p2_card = p2.get_tactical_card()

        result = rps.judge(p1_card, p2_card)

        if result != 0 and (p1_card == 0 or p2_card == 0):
                if result == 1:
                    p1.set_accept_heavy_blows(False)
                else:
                    p2.set_accept_heavy_blows(False)