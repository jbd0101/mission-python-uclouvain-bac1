a = ["bonjour","manger","appeler","aarlon"]
b = ["mourir","dire","arnaquer",'boir']

def sortL(array):
  c=[]
  while array:
    minimum = ""
    for e in array:
      if(e<minimum or minimum==""):
        minimum = e
    c.append(minimum)
    array.remove(minimum)
  print(c)
sortL(a)
