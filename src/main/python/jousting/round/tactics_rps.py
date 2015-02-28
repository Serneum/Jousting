from jousting.round.phase import Phase
from jousting.util import rps


class TacticsCardRPS(Phase):
    def do_tactics_rps(self):
        p1 = self._controller.get_p1()
        p2 = self._controller.get_p2()

        if not p1.get_failed_to_start() and not p2.get_failed_to_start():
            p1_card = p1.get_tactical_card()
            p2_card = p2.get_tactical_card()

            result = rps.judge(p1_card, p2_card)

            if result == 1:
                if p1_card == rps.SHIELD:
                    p1.set_accept_heavy_blows(False)
                else:
                    p1.set_won_rps(True)
            elif result == 2:
                if p2_card == rps.SHIELD:
                    p2.set_accept_heavy_blows(False)
                else:
                    p2.set_won_rps(True)