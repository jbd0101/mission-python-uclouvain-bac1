#Developpe par jean-christophe bauduin,groupe 11.13

from XYRobot import *
import unittest
import graphics

class TestXYRobot(unittest.TestCase):
    def test_position_ini (self):
        r2d2 = XYRobot("R2-D2")
        self.assertEqual(r2d2.position(), (0,0)), "your robot is not at the required place"
    def test_position_after_move(self):
        r2d2 = XYRobot("R2-D2")
        r2d2.moveforward(15)
        r2d2.movebackward(10)
        r2d2.turnleft()
        r2d2.moveforward(10)
        r2d2.turnright()
        r2d2.moveforward(15)
        self.assertEqual(r2d2.position(), (20,-10)), "your robot is not at the required place"
    def test_history(self):
        rob = XYRobot("no memory")
        rob.moveforward(15)
        rob.turnright()
        rob.movebackward(100)
        rob.moveforward(15)
        rob.turnleft()
        rob.moveforward(90)
        self.assertEqual(rob.history()[0],("moveforward",15),"l historique est corrompu")
        self.assertNotEqual(rob.position(), (0,0)), "Tu as fait du sur place !"
        rob.unplay()
        x,y=rob.position()
        x,y = int(x),int(y)
        self.assertEqual((x,y), (0,0)), "your robot is not at the required place"








if __name__ == '__main__':
    unittest.main()
