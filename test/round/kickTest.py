from kick import Kick
from controller import Controller
import unittest

class KickTest(unittest.TestCase):

    def test_kick(self):
        controller = Controller()
        phase = Kick(controller)
        phase.do_kick()
        self.assertNotEquals(phase._controller.get_p1(), phase._controller.get_p2())

    def test_knight_move_during_kick(self):
        controller = Controller()
        phase = Kick(controller)

        for i in range(1000):
            phase.do_kick()
            self.assertNotEquals(0, phase._controller.get_p1().get_current_position())
            self.assertNotEquals(0, phase._controller.get_p2().get_current_position())

    def test_swap_logic(self):
        controller = Controller()
        p1 = controller.get_p1()
        p2 = controller.get_p2()
        controller.set_p1(p2)
        controller.set_p2(p1)

        self.assertEquals(controller.get_p1(), p2)
        self.assertEquals(controller.get_p2(), p1)
        self.assertNotEquals(controller.get_p1(), controller.get_p2())