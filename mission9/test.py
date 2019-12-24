from article import Article
from mission9 import *
"""
   Classe de test initiale pour la classe Facture.
   initialement :
   @author Kim Mens
   @version 18 novembre 2018
   (code adaptÃ© du code java de Charles Pecheur)
  fait par jean-christophe bauduin

"""

class TestFactureInitial :

    articles = [ Article("laptop 15\" 8GB RAM", 743.79),
                 Article("installation windows", 66.11),
                 Article("installation wifi", 45.22),
                 Article("carte graphique", 119.49)
                 ]

    @classmethod
    def run(cls) :
        assert str(ArticleReparation(2))=="Reparation (2.00 heures): 90.00"
        p1 = Piece("test1",3,2)
        art1 = ArticlePiece(5,p1)
        p2= Piece("test2",1,1)
        art2= ArticlePiece(2,p2)
        f = Facture("demo",[art1,art1,art1,art2])
        assert p1 != p2
        assert p1 == p1
        assert p1.poids()==2
        assert p1.tva_reduit()==False
        assert art1.tva() ==3.15
        assert f.nombre(p2) == 2
        assert f.nombre(p1) == 15
        assert "4 articles" in str(f)
        f.printLivraison()


if __name__ == "__main__":
    TestFactureInitial.run()
