"""
    Un article de facture simple, comprenant un descriptif et un prix.

    @author Kim Mens
    @version 18 novembre 2018
    (code adaptÃ© du code java de Charles Pecheur)
"""

class Article :

    __taux_tva = 0.21   # TVA a 21%

    @classmethod
    def getTVA(cls):
        return cls.__taux_tva

    def __init__(self,d,p):
        """
        Cree un article avec description d et prix p.
        """
        self.__description = d
        self.__prix = p

    def description(self):
        """
        Retourne la description de cet article.
        """
        return self.__description

    def prix(self):
        """
        Retourne le prix (HTVA) de cet article.
        """
        return self.__prix

    def taux_tva(self):
        """
        Retourne le taux de TVA (mÃªme valeur pour chaque article)
        """
        return Article.getTVA()

    def tva(self):
        """
        Retourne la TVA sur cet article
        """
        return self.prix() * self.taux_tva()

    def prix_tvac(self):
        """
        Retourne le prix de l'article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        Retourne un texte decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f}".format(self.description(), self.prix())
