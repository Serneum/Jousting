class Knight:
    def __init__(self, name):
        self.__name = " ".join(["Sir", name])
        self.__bruises = 0
        self.__curr_pos = 0
        self.__tactical_card = -1
        self.__accept_heavy_blows = True
        self.__points = 0
        self.__fail_start = False
        self.__fail_start_count = 0
        self.__won_rps = False
        self.__strike_modifier = 0
        self.__unhorsed = False

    def get_name(self):
        return self.__name

    def move(self, spaces):
        self.__curr_pos += spaces

    def get_current_position(self):
        return self.__curr_pos

    def add_bruise(self):
        self.__bruises += 1

    def get_bruises(self):
        return self.__bruises

    def set_tactical_card(self, card):
        self.__tactical_card = card

    def get_tactical_card(self):
        return self.__tactical_card

    def set_accept_heavy_blows(self, accept):
        self.__accept_heavy_blows = accept

    def get_accept_heavy_blows(self):
        return self.__accept_heavy_blows

    def add_fail_start(self):
        self.__fail_start_count += 1

    def get_failed_to_start(self):
        if self.get_current_position() < 7:
            self.__fail_start = True
        return self.__fail_start

    def add_points(self, points):
        self.__points += points

    def get_points(self):
        return self.__points

    def get_disqualified(self):
        return self.__fail_start_count >= 2

    def set_won_rps(self, won_rps):
        self.__won_rps = won_rps

    def get_won_rps(self):
        return self.__won_rps

    def set_strike_modifier(self, modifier):
        self.__strike_modifier = modifier

    def get_strike_modifier(self):
        return self.__strike_modifier

    def set_unhorsed(self, unhorsed):
        self.__unhorsed = unhorsed

    def get_unhorsed(self):
        return self.__unhorsed

    def reset_for_round(self):
        self.__curr_pos = 0
        self.__fail_start = False