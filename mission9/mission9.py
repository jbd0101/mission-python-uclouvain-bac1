"""
  fait par jean-christophe bauduin le 20/11

"""

from article import *
import test,random

class ArticleReparation(Article):
  """docstring for ArticleReparation"""
  def __init__(self,duree):
    self.duree = duree
  def prix(self):
    return self.duree*35+20
  def description(self):
    return("Reparation ({0:.2f} heures)".format(self.duree))

class Piece:
  def __init__(self,description,prix,poids=0,fragile=False,tvareduite=False):
    self.__description = description
    self.__prix = prix
    self.__poids = poids
    self.__fragile = fragile
    self.__tvareduite = tvareduite
  def prix(self):
    return(self.__prix)
  def description(self):
    return(self.__description)
  def poids(self):
    return self.__poids
  def fragile(self):
    return self.__fragile
  def tva_reduit(self):
    return self.__tvareduite
  def __eq__(self,other):
    return(self.__prix == other.prix() and self.__description==other.description())
  def __str__(self):
    return("{0}".format(self.description()))

class ArticlePiece(Article):
  __tvareduite = 0.06
  """docstring for ArticlePiece"""
  @classmethod
  def getTTVAReduite(cls):
    return cls.__tvareduite
  def __init__(self, quantite,piece):
    super().__init__(piece.description(),piece.prix())
    self.__quantite = quantite
    self.__piece = piece
  def tva(self):
    return self.prix() * (ArticlePiece.getTTVAReduite() if self.__piece.tva_reduit() else ArticlePiece.getTVA())
  def quantite(self):
    return(self.__quantite)
  def piece(self):
    return(self.__piece)
  def prix(self):
    return(self.__piece.prix()*self.__quantite)
  def description(self):
    return("{} * {} ".format(self.quantite(),str(self.piece())))



class Facture :
  def __init__(self, description, articles,uuid=random.randint(0,999)):
    """
    CrÃ©e une facture avec une description (titre) et un liste d'articles.
    """
    self.__reference = description
    self.__articles = articles
    self.__uuid =uuid
  def nombre(self,pce):
    """
    Retourne le nombre d'exemplaires de la piÃ¨ce pce dans la facture, en totalisant sur tous les articles qui concernent cette piÃ¨ce.
    """
    r = 0
    for a in self.__articles:
      r += a.quantite() if (a.piece() == pce) else 0
    return r
  def description(self):
    """
    Retourne la description de cette facture.
    """
    return self.__reference

  def articles(self):
    """
    Retourne la liste des articles de cette facture.
    """
    return self.__articles

  def __str__(self):
    """
    Retourne la reprÃ©sentation string d'une facture, Ã  imprimer avec la mÃ©thode print().
    """
    s = self.entete_str()
    poids = 0
    qt = 0
    for art in self.articles() :
        s += self.article_str(art)
        qt+=art.quantite()
        poids += art.piece().poids() * art.quantite()
    s += self.totaux_str(qt, poids)
    return s

  def entete_str(self):
    """
    Imprime l'entÃªte de la facture, comprenant le descriptif et les tÃªtes de colonnes.
    """
    e = "Livraison - Facture #{:5} : {:10} \n".format(self.__uuid,self.__reference)
    e += self.barre_str()
    e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description"," poids/pce","Nombre","poids")
    e += self.barre_str()
    return e

  def barre_str(self):
    """
    Retourne un string reprÃ©sentant une barre horizontale sur la largeur de la facture.
    """
    b = ""
    barre_longeur = 83
    for i in range(barre_longeur):
        b += "="
    return b + "\n"

  def article_str(self, art):
    """
    Retourne un string correspondant Ã  une ligne de facture pour l'article art
    """
    return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.piece().poids(), art.quantite(), art.piece().poids()*art.quantite())

  def totaux_str(self, quantite, poids):
    """
    Retourne un string reprÃ©sentant une ligne de facture avec les totaux prix et tva, Ã  imprimer en bas de la facture
    """
    b = self.barre_str()
    b += "| {0:10} {1:30}| {2:10} | {3:10.2f} | {4:10.2f} |\n".format(len(self.__articles),"articles","",quantite, poids)
    b += self.barre_str()
    return b



  # This method needs to be added during Etape 5 of the mission
  def printLivraison(self):
    print(str(self))

  def livraison_str(self):
    """
    Cette mÃ©thode est une mÃ©thode auxiliaire pour la mÃ©thode printLivraison
    """

