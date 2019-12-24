#dev par Jean-Christophe Bauduin
#le 6/11
import re
def readfile(filename):
  """
    Lit le fichier et le renvoit en une string
    args:
    filename : chemin vers le fichier (string)
    return:
    file text
  """
  r = ""
  try:
    with open(filename,"r") as f:
      r = f.read()
  except Exception as e:
    r = ("Une erreur est survenue")
  return(r)
def cleanup(txt):
  """
    cleanup string
    args:
    text in string
    return
    cleaned text (string)
  """
  txt = re.sub(r"[\.\,\;\-\!\?\']*","",txt.lower())
  return(txt)
def get_words(line):
  """
    from line to list : split at space
    args:
    line in string
    return
    array of words
  """
  return(cleanup(line).split())
def get_lines(words,index):
  """
    search if the words in the arrays appears in the same line and returns in which one
    args:
    words : array of words
    index: create_index() function
    return
    array of positions
  """
  presents = []
  Lwords = len(words)
  r = []
  for word in words:
    word = cleanup(word)
    try:
      presents.extend(list(index[word]))
    except Exception as e:
      pass
  for p in set(presents):
    c = presents.count(p)
    if(c>=Lwords):
      r.append(p)
  return(r)
def create_index(filename):
  """
    cree l index des positions des elements
    args:
    le fichier (path to file)
    return
    dictionnaire avec cle : le mot, et un sous dictionnaire avec la cle la position (ligne) et le nombre d occurence
  """
  lines = cleanup(readfile(filename)).split("\n")
  dico = {}
  for index,line in enumerate(lines):
    for word in set(get_words(line)):
      dico
      if(dico.get(word)==None):
        dico[word]={}
      value = line.count(word)
      if(value > 0):
        dico[word][index] = value
  return(dico)

# index = create_index("test.txt")
# words = ["lorem","dolor"]
# get_lines(words,index)
