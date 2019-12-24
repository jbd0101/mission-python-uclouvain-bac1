"""
Developpe par : Jean-Christophe Bauduin
"""

import re
def is_adn(s):
  """
  Vérifie si une string respecte la règle de l'ADN
  pre: `s` String d'adn
  post: True si c'est de l'adn False si vide ou ne respecte pas les règles de l'adn
  """
  r = False
  if(len(s)>0):
    s = re.sub(r"([ATCGatcg]*)","",s)
    r = True if s=="" else False
  return(r)

def positions(s, p):
  """
  Renvoit la position d'un élément dans un string
  pre: `s` String, adn
       `p` String, element recherche
  post: True si c'est de l'adn False si vide ou ne respecte pas les règles de l'adn
  """
  s = s.lower()
  p = p.lower()
  r = []
  for m in re.finditer(p, s):
    r.append(m.start())
  return(r)

def distance_h(s1,s2):
  """
  Calcule la distance entre 2 strings (soit regarder le nombre d'elements qui different)
  pre:
  `s1` String d'adn
  `s2` String d'adn
  les 2 distances doivent etre egale
  post: Le nombre de caracteres qui different ou None si les 2 strings n'ont pas la meme taille
  """
  count = 0
  if(len(s1)==len(s2)):
    for c1,c2 in zip(s1.lower(),s2.lower()):
      count += 0 if c1==c2 else 1
    return(count)
  else:
    return None
def reverser(s):
  r = ""
  for c in reversed(s):
    r+=c
  return(r)
def plus_long_palindrome(text):
  """
  Renvoit le plus long palindrome
  pre:
  `text` String
  post: Renvoit le plus grand palindrome
  """
  maximum = 0
  palindrome = ""
  for i in range(len(text)):
    string = text[i:]
    for n in reversed(range(2,len(string)+1)):
      possibilite = string[:n]
      inv = reverser(possibilite)
      if(possibilite == inv and maximum <n):
        maximum = n
        palindrome = possibilite
        break
  return(palindrome)
"""
version basique

def distances_matrice(l):
  r = []
  for e in l:
    r.append(list(map(lambda p: distance_h(e,p),l)))
  return(r)
"""
#version fun
def distances_matrice(l):
  return(list(map(lambda e: list(map(lambda p: distance_h(e,p),l)),l)))
