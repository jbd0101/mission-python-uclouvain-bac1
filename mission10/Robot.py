import copy
#Developpe par jean-christophe bauduin,groupe 11.13
class Robot:
  def __init__(self):
    self.__history = []
  def history(self):
    return self.__history
  def pushHistory(self,action,arg):
    self.__history.append((action,arg))
  def unplay(self):
    todo = copy.deepcopy(self.__history)
    reverse ={
      "moveforward": "movebackward",
      "movebackward": "moveforward",
      "turnright": "turnleft",
      "turnleft": "turnright"
    }
    for a,arg in reversed(todo):
      to_exec="self."+reverse[a]+"("+str(arg)+")"
      eval(to_exec)
    self.__history=[]
