# developpé par Jean-Christophe Bauduin
# init des variables utilises
max = 10 # le nombre de fin de la boucle
somme_carre = 0 # la variable qui va contenir la somme des carres
i = 1 # l'iterateur

# debut de la boucle
while i<=max:
    carre = i**2 #le carre
    somme_carre += carre # on ajoute la somme des carres par le carre actuel
    somme_par_calc = i*(i+1)*(2*i+1)//6 # la somme des carres par la formule donnee
    print(i,"\t",carre,"\t",somme_carre,"\t",somme_par_calc) # on affiche le tout
    i+=1 # on incremente l'iterateur
