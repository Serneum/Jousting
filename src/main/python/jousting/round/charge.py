from jousting.round.phase import Phase
from jousting.util.dice import D6, roll


class Charge(Phase):
    def do_charge(self):
        p1 = self._controller.get_p1()
        p2 = self._controller.get_p2()
        while not self.check_point_of_contact():
            p1_move = self.limit_movement(self.roll_movement())
            p1.move(p1_move)

            p2_move = self.limit_movement(self.roll_movement())
            p2.move(p2_move)

        p1.determine_failed_to_start()
        p2.determine_failed_to_start()

        if p1.get_failed_to_start():
            p1.add_fail_start()
        elif p2.get_failed_to_start():
            p2.add_fail_start()

    def roll_movement(self):
        # Roll two dice and subtract a third die roll from their value
        roll_val = roll(D6, 2, -1 * roll(D6, 1))
        roll_val = 1 if roll_val < 0 else roll_val
        return roll_val

    def limit_movement(self, movement):
        p1 = self._controller.get_p1()
        p2 = self._controller.get_p2()
        # There are 24 spaces on the field, so check how far the players are from each other
        spaces_to_contact = 24 - p1.get_current_position() - p2.get_current_position()
        return movement if movement < spaces_to_contact else spaces_to_contact

    def check_point_of_contact(self):
        p1 = self._controller.get_p1()
        p2 = self._controller.get_p2()
        # There are 24 spaces on the field, so if the positions add to 24 the players are at the point of contact
        return p1.get_current_position() + p2.get_current_position() == 24
