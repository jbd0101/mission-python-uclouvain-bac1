#Developpe par jean-christophe bauduin,groupe 11.13

import turtle
import Robot

class TurtleBot(Robot.Robot):
  def __init__(self,n):
    super().__init__()
    self.__nom__ = n  # nom du robot
    self.tortue = turtle.Turtle()
    self.tortue.speed("fastest")
    # self.resetTopLeft()
  def getangle(self):
    return self.tortue.heading()
  def position(self):
    return self.tortue.pos()
  def resetTopLeft(self):
    """Remet la tortue en haut à gauche oriente vers l'est.

    pre:
    La tortue `tortue` est initialisée.
    post: La tortue est placée en haut à gauche et orienté vers l'est
    """
    self.tortue.penup()
    self.tortue.setx(-turtle.window_width()//2)
    self.tortue.sety(turtle.window_height()//2)
    self.tortue.seth(0) #je regarde vers l'est (cf https://docs.python.org/2/library/turtle.html)
    self.tortue.pendown()
  def moveforward(self,d):
    self.pushHistory("moveforward",d)
    self.forward(d)
    return self.position()
  def movebackward(self,d):
    self.pushHistory("movebackward",d)
    self.forward(-d)
    return self.position()
  def turnleft(self):
    self.pushHistory("turnleft","")
    self.tortue.left(90)
    return self.position()
  def turnright(self):
    self.pushHistory("turnright","")

    self.tortue.right(90)
    return (0,0)
  def forward(self,width):
    """Avance la tortue de `width` vers l'est et oriente la tortue vers l'est

    pre: `width`: la distance à parcourir (en px)
    La tortue `tortue` est initialisee.
    post: La tortue est avancée de `width` vers l'est
    """
    self.tortue.forward(width)

# t = TurtleBot("ll")
# t.moveforward(40)
# t.turnleft()
# t.moveforward(100)
# t.turnright()
# t.movebackward(200)
# t.unplay()
# print(t.position())
