"""
developpe par jean-christophe bauduin, groupe 11.13
"""
class Duree:
  """Classe qui gere la duree"""
  def __init__(self,h=0, m=0, s=0):
    super(Duree, self).__init__()
    if(m < 0 or m>60):
      raise ValueError("M doit etre comprit entre 0 et 60 clampin")
    if(s < 0 or s>60):
      raise ValueError("S doit etre comprit entre 0 et 60 clampin")
    self.duree = h*60*60+m*60+s

  def toSecondes(self) :
    """
    Retourne le nombre total de secondes de cette instance de Duree (self).
    """
    return(self.duree)

  def delta(self,d) :
    """
    Retourne la différence entre cette instance de Duree (self) et la Duree d passée en paramètre,
    en secondes (positif si ce temps-ci est plus grand).
    """
    return(abs(d-self.duree))

  def apres(self,d):
    """
    Retourne True si cette instance de Duree (self) est plus grand que la Duree d passée en paramètre;
    retourne False sinon.
    """
    return True if d>self.duree else False

  def ajouter(self,d):
    """
    Ajoute une autre Duree d à cette instance de Duree (self).
    Corrige de manière à ce que les minutes et les secondes soient dans l'intervalle [0..60[,
    en reportant au besoin les valeurs hors limites sur les unités supérieures
    (60 secondes = 1 minute, 60 minutes = 1 heure).
    """
    self.duree+=d
    return(self.toHMS())
  def __str__(self):
    """
    Retourne cette durée sous la forme de texte "heures:minutes:secondes".
    Astuce: la méthode "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
    retourne le String désiré avec les nombres en deux chiffres en ajoutant
    les zéros nécessaires.
    """
    h,m,s = self.toHMS()
    return("{:02}:{:02}:{:02}".format(h,m,s))
  def toHMS(self):
    """
    Retourne la duree stockee en seconde en heure minute seconde
    args none
    returns h[heure],m[minute],s[seconde]

    """
    m,s = divmod(self.duree,60)
    h,m = divmod(m,60)
    return(h,m,s)

class Chanson:
  """la classe chanson"""
  def __init__(self, t,a,d):
    super(Chanson, self).__init__()
    self.t = t
    self.a = a
    self.d = d
  def __str__(self):
    """
    Retourne un String décrivant cette chanson sous le format "TITRE - AUTEUR - DUREE".
    Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
    """
    return("{} - {} - {}".format(self.t,self.a,self.d))

class Album:
  number_of_albums=0
  def __init__(self):
    self.chansons=[]
    Album.number_of_albums += 1
    self.albumId = Album.number_of_albums
  def duree(self):
    """
    Renvoit la duree totale en seconde de l album
    """
    t= 0
    for c in self.chansons:
      t += c.d.toSecondes()
    return(t)
  def length(self):
    """
    REtourne la longueur de l'alumb (nombre de musique quoi)
    """
    return(len(self.chansons))
  def dureeString(self):
    d = self.duree()
    m,s = divmod(d,60)
    h,m = divmod(m,60)
    return("{:02}:{:02}:{:02}".format(h,m,s))

  def add(self,chanson):
    if((self.duree()+chanson.d.toSecondes())//60 >= 75 or self.length() >= 100):
      return False
    else:
      self.chansons.append(chanson)
      return True
  def __str__(self):
    length = self.length()
    r = "Album {} ({} chansons, {})\n".format(self.albumId,length,self.dureeString())
    maxL = len(str(length))
    for i,c in enumerate(self.chansons):
      r+="{}: {} - {} - {}\n".format(str(i+1).zfill(maxL),c.t,c.a,str(c.d))
    return(r)


if __name__ == "__main__":
  db = ""
  with open("music-db.txt","r") as f:
    db = f.readlines()

  album = Album()
  for i,line in enumerate(db):
    musique = line.split()
    titre = musique[0]
    auteur = musique[1]
    minutes = int(musique[2])
    secondes = int(musique[3])
    duree = Duree(0,minutes,secondes)
    chanson = Chanson(titre,auteur,duree)
    ajout = album.add(chanson)

    if(not ajout):
      print(album)
      album=None
      album = Album()
      album.add(chanson)
      duree =None
      chanson =None
  print(album)


