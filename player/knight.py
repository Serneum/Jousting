from dice import roll, D3, D6

class Knight:
    def __init__(self):
        self.bruises = 0
        self.curr_pos = 0
        self.tactical_card = -1
        self.accept_heavy_blows = True
        self.points = 0
        self.fail_start_count = 0
        self.strike_modifier = 0
        self.unhorsed = False

    def move(self, spaces):
        self.curr_pos += spaces

    def get_current_position(self):
        return self.curr_pos

    def add_bruise(self):
        self.bruises += 1

    def get_bruises(self):
        return self.bruises

    def set_tactical_card(self, card):
        self.tactical_card = card

    def get_tactical_card(self):
        return self.tactical_card

    def set_accept_heavy_blows(self, accept):
        self.accept_heavy_blows = accept

    def get_accept_heavy_blows(self):
        return self.accept_heavy_blows

    def add_fail_start(self):
        self.fail_start_count += 1

    def get_failure_to_start(self):
        return self.curr_pos < 7

    def add_points(self, points):
        self.points += points

    def get_points(self):
        return self.points

    def get_disqualified(self):
        return self.fail_start_count >= 2

    def set_strike_modifier(self, modifier):
        self.strike_modifier = modifier

    def get_strike_modifier(self):
        return self.strike_modifier

    def set_unhorsed(self, unhorsed):
        self.unhorsed = unhorsed

    def get_unhorsed(self):
        return self.unhorsed