#dev par Jean christophe bauduin et timour petit

import difflib #uniquement pour l'amusemnt dans la partie recherche , entierement facultatif
import re #utilise pour le split ameliore des listes
print("Bienvenue sur votre assistant")
file = ""
dictionnary=[]
needExit= False

def loadFile(arg):
  global file
  try:
    with open(arg,"r") as f:
      file = f.read()
  except Exception as e:
    file=""
    return("erreur document")
  return("Fichier charge")

def binary_search ( name, list_of_names ):
  first = 0
  last = len(list_of_names)-1
  found = False

  while first<=last and not found:
    middle = (first + last)//2
    if list_of_names[middle] == name:
      found = True

    else:
      if name < list_of_names[middle]:
        last = middle-1
      else:
        first = middle+1
  return list_of_names[(first+last)//2]

def info():
  lines = len(file.split("\n"))
  caracs = len(file)
  return("{0} Lignes \n{1} caracteres".format(lines,caracs))
def dictionnary():
  global dictionnary
  dictionnary = sorted(re.split("[\s]",file)) #le split par regex est FACULTATIF , mais tres utilie pour le dictionnaire avec numeros...
  return("dictionnaire chargé, contient {0} mots".format(len(dictionnary)))
def calcSum(nmbrs):
  total = 0
  for c in nmbrs:
    total += float(c)
  return(total)
def sum(nmbrs):
  nmbrs = nmbrs.split(" ")
  return("Total : {0}".format(calcSum(nmbrs)))
def handleHelp():
  return("""
Votre assistant personnelle possede plusieurs fonctions
- file (charge un fichier)
- sum (somme des argument)
- avg (moyenne des argument)
- dictionnary (charge le dictionnaire)
- info (donne des infos sur votre fichier)
- search (cherche )
- exit
    """)
def exit():
  global needExit
  needExit = True
  return("A bientot")
def avg(nmbrs):
  nmbrs = nmbrs.split(" ")
  moyenne = (calcSum(nmbrs)/len(nmbrs))
  return("Moyenne : {0}".format(moyenne))

def search(q):
  methodePackage= ""
  methodeSearchBinary= ""
  try:
    methodePackage= difflib.get_close_matches(q,dictionnary)[-1]
  except Exception as e:
    return("méthode de recherche par librairie n'a rien trouve")
  try:
    methodeSearchBinary = binary_search(q,dictionnary)
  except Exception as e:
    methodeSearchBinary= ""
    return("La recherche par binary search a planté désolé")
  return("Résultats de la recherche : \n-{0} (binary search)\n-{1} methode de difflib".format(methodeSearchBinary,methodePackage))
def dispatch(c):
  c = c.split(" ")
  commande = c[0]
  arg = ""
  hasArg = False
  r = ""
  if(len(c)>=2):
    arg = " ".join(c[1:])
    hasArg = True

  if("file" in commande and hasArg):
    r = loadFile(arg)
  elif("sum" in commande and hasArg):
    r = sum(arg)
  elif("avg" in commande and hasArg):
    r = avg(arg)
  elif("exit" in commande):
    r = exit()
  elif("help" in commande):
    r = handleHelp()
  else:
    if(file==""):
      r = "Document non charge"
    else:
      if("info" in commande):
        r = info()
      elif("dictionnary" in commande):
        r = dictionnary()
      elif("search" in commande and hasArg):
        r = search(arg)
  return(r)

if __name__ == "__main__":
  while not needExit:
    c = input("> ")
    print(dispatch(c))
