from knight import Knight
from kick import Kick
from charge import Charge
from tactics_rps import TacticsCardRPS
from lance import TasteOfTheLance

class Controller:
    def __init__(self):
        self.p1 = Knight()
        self.p2 = Knight()
        self.kick = Kick(self)
        self.charge = Charge(self)
        self.tactics = TacticsCardRPS(self)
        self.lance = TasteOfTheLance(self)

    def do_game(self):

        for i in range(3):
            self.do_round()
            p1 = self.get_p1()
            p2 = self.get_p2()
            if p1.get_unhorsed() or p2.get_unhorsed():
                break

            print " ".join(["At the end of round", str(i + 1), "Player 1 has", str(p1.get_points()), "points, and Player 2 has", str(p2.get_points()), "points."])
            self.reset_player_positions()

        if p1.get_unhorsed():
            print "Player 2 wins by unhorsing Player 1"
        elif p2.get_unhorsed():
            print "Player 1 wins by unhorsing Player 2"
        else:
            p1_points = p1.get_points()
            p2_points = p2.get_points()
            if p1_points > p2_points:
                print " ".join(["Player 1 wins", str(p1_points), "to", str(p2_points)])
            elif p2_points > p1_points:
                print " ".join(["Player 2 wins", str(p2_points), "to", str(p1_points)])
            else:
                print " ".join(["Player 1 and Player 2 tie with", str(p1_points), "points"])

    def do_round(self):
        self.kick.do_kick()
        self.charge.do_charge()
        self.tactics.do_tactics_rps()
        self.lance.do_taste_of_the_lance()


    def get_p1(self):
        return self.p1

    def get_p2(self):
        return self.p2

    def set_p1(self, p1):
        self.p1 = p1

    def set_p2(self, p2):
        self.p2 = p2

    def reset_player_positions(self):
        p1 = self.get_p1()
        p2 = self.get_p2()

        p1.move(-1 * p1.get_current_position())
        p2.move(-1 * p2.get_current_position())