from jousting.round.phase import Phase
from jousting.util.dice import D6, roll
from jousting.util.rps import SHIELD


class TasteOfTheLance(Phase):
    def do_taste_of_the_lance(self):
        p1 = self._controller.get_p1()
        p2 = self._controller.get_p2()

        p1_tactical_modifier = 1 if p1.get_won_rps() and p1.get_tactical_card() != SHIELD else 0
        p2_tactical_modifier = 1 if p2.get_won_rps() and p2.get_tactical_card() != SHIELD else 0
        self.determine_strike_modifier(p1, p1_tactical_modifier)
        self.determine_strike_modifier(p2, p2_tactical_modifier)

        self.strike_roll(p1, p2)
        if not p2.get_unhorsed:
            self.strike_roll(p2, p1)

    def determine_strike_modifier(self, player, tactical=0):
        if player.get_current_position() <= 12:
            position = 0
        elif player.get_current_position() <= 15:
            position = 1
        else:
            position = 2
        total_modifier = position + tactical - player.get_bruises()
        total_modifier = total_modifier if total_modifier >= 0 else 0
        player.set_strike_modifier(total_modifier if total_modifier >= 0 else 0)

    # 1-2: Glancing blow. Effectively a miss. No points scored
    # 3-4: Light blow. Score 2 points
    # 5-6: Heavy blow. Score 3 points. Roll for effects
    def strike_roll(self, player, opponent):
        modifier = player.get_strike_modifier()
        strike_roll = roll(D6, 1, modifier)

        if (not opponent.get_accept_heavy_blows()) and strike_roll > 4:
            strike_roll = 4

        if 3 <= strike_roll < 5:
            player.add_points(2)
        elif strike_roll >= 5:
            player.add_points(3)
            self.heavy_blow_roll(opponent)

    # 1-3: No effect
    # 4-5: Bruise opponent
    # 6: Unhorse opponent. Win joust
    def heavy_blow_roll(self, opponent):
        heavy_roll = roll(D6)
        if 4 <= heavy_roll < 6:
            opponent.add_bruise()
        elif heavy_roll == 6:
            opponent.set_unhorsed(True)

    # 1-3: Lance not broken
    # 4-6: Lance broken. Score 1 point
    def lance_break_roll(self, player):
        break_roll = roll(D6)
        if break_roll >= 4:
            player.add_points(1)