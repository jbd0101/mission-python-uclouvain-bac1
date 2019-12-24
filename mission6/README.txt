dev par Jean christophe bauduin et timour petit
le 30/10/19

Tout est operationnelle, mais nous etions pas sur de bien comprendre ce que nous devions faire pour la partie dictionnaire, on a donc fait ce qu on croyait devoir faire.

Par amusement, nous avons utilise 2 methodes pour la recherche: le binary search et un package .

Nous avons utilise la 2 e liste de vocabulaire qui est comme suit:
<chiffre> <chiffre> <mot>
Nous avions donc 2 choix pour separer le mot :
soit
a) remplacer les \n par des espaces et ensuite faire un split sur les espaces
b) utiliser une regex
Nous trouvions la regex plus fun, on a donc utilise les regex , mais si vous voulez ne pas utiliser les regex
il suffit de faire
string.replace("\n"," ").split(" ")
