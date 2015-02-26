import random

from jousting.player.knight import Knight
from jousting.round.kick import Kick
from jousting.round.charge import Charge
from jousting.round.tactics_rps import TacticsCardRPS
from jousting.round.lance import TasteOfTheLance
from jousting.util.rps import SHIELD, COUNTER, LUNGE


class Controller:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2
        self.__kick = Kick(self)
        self.__charge = Charge(self)
        self.__tactics = TacticsCardRPS(self)
        self.__lance = TasteOfTheLance(self)

    def do_game(self):
        p1 = None
        p2 = None
        p1_name = None
        p2_name = None

        for i in range(3):
            self.do_round()
            p1 = self.get_p1()
            p2 = self.get_p2()
            p1_name = p1.get_name()
            p2_name = p2.get_name()

            if p1.get_unhorsed() or p2.get_unhorsed():
                break
            if p1.get_disqualified() or p2.get_disqualified():
                break

            print " ".join(["At the end of round", str(i + 1), p1_name, "has", str(p1.get_points()),
                            "points, and", p2_name, "has", str(p2.get_points()), "points."])
            self.reset_players_for_new_round()

        if p1.get_unhorsed():
            print " ".join([p2_name, "wins by unhorsing", p1_name])
        elif p2.get_unhorsed():
            print " ".join([p1_name, "wins by unhorsing", p2_name])
        elif p1.get_disqualified():
            print " ".join([p1_name, "has failed to start twice and has been disqualified."])
        elif p2.get_disqualified():
            print " ".join([p2_name, "has failed to start twice and has been disqualified."])
        else:
            p1_points = p1.get_points()
            p2_points = p2.get_points()
            if p1_points > p2_points:
                print " ".join([p1_name, "wins", str(p1_points), "to", str(p2_points)])
            elif p2_points > p1_points:
                print " ".join([p2_name, "wins", str(p2_points), "to", str(p1_points)])
            else:
                print " ".join([p1_name, "and", p2_name, "tie with", str(p1_points), "points"])

    def do_round(self):
        p1 = self.get_p1()
        p2 = self.get_p2()

        p1.set_tactical_card(random.choice([SHIELD, COUNTER, LUNGE]))
        p2.set_tactical_card(random.choice([SHIELD, COUNTER, LUNGE]))

        self.__kick.do_kick()
        self.__charge.do_charge()

        if p1.get_failed_to_start():
            print " ".join([p1.get_name(), "failed to start and the round is over."])
        elif p2.get_failed_to_start():
            print " ".join([p2.get_name(), "failed to start and the round is over."])
        else:
            self.__tactics.do_tactics_rps()
            self.__lance.do_taste_of_the_lance()

    def get_p1(self):
        return self.__p1

    def get_p2(self):
        return self.__p2

    def set_p1(self, p1):
        self.__p1 = p1

    def set_p2(self, p2):
        self.__p2 = p2

    def reset_players_for_new_round(self):
        self.get_p1().reset_for_round()
        self.get_p2().reset_for_round()