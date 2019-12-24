import turtle             # module des graphiques tortue
tortue = turtle.Turtle()     # créer une nouvelle tortue
tortue.speed("fastest")      # tracé rapide
bigSize= 200
littleSize= 100
def resetTopLeft():
  """Remet la tortue en haut à gauche oriente vers l'est.

  pre:
  La tortue `tortue` est initialisée.
  post: La tortue est placée en haut à gauche et orienté vers l'est
  """
  tortue.penup()
  tortue.setx(-turtle.window_width()//2)
  tortue.sety(turtle.window_height()//2)
  tortue.pendown()
def margin_x(width):
  """Avance la tortue de `width` vers l'est et oriente la tortue vers l'est

  pre: `width`: la distance à parcourir (en px)
  La tortue `tortue` est initialisee.
  post: La tortue est avancée de `width` vers l'est
  """
  tortue.penup()
  tortue.seth(0) #je regarde vers l'est (cf https://docs.python.org/2/library/turtle.html)
  tortue.forward(width)
  tortue.pendown()
def margin_y(dist):
  """Avance la tortue de `dist` vers le sud et oriente la tortue vers l'est

  pre: `dist`: la distance à parcourir (en px)
  La tortue `tortue` est initialisée.
  post: La tortue est avancée de `width` vers le sud
  """
  tortue.penup()
  tortue.seth(270)
  tortue.forward(dist)
  tortue.seth(0)
  tortue.pendown()

def star(width):
  """Dessine une etoile avec chaque cote de largeur `width`

  pre: `width`: la taille de chaque côté de l'etoile
  La tortue `tortue` est initialisée.
  post: une étoile (jaune) est descinée
  """
  tortue.fillcolor("yellow")
  tortue.begin_fill()
  for i in range(5):
    tortue.forward(width)
    tortue.right(140)
    tortue.forward(width)
    tortue.right(-68)
  tortue.end_fill()

def square(size, color):
  """Trace un carreq plein de taille `size` et de couleur `color`.

  pre: `color` spécifie une couleur.
       La tortue `tortue` est initialisée.
       La tortue est placée à un sommet et orientée en direction d'un
       côté du carré.
  post: Le carré a été tracé sur la droite du premier côté.
        La tortue est à la même position et orientation qu'au départ.
  """
  tortue.color(color)
  tortue.pendown()
  tortue.begin_fill()
  for i in range(4):
      tortue.forward(size)
      tortue.right(90)
  tortue.end_fill()
  tortue.penup()
def rectangle(sizeX,sizeY, color):
  """Dessine un resctange de `sizeX` x `sizeY` en la couleur `color`

  pre: `sizeX`: largeur (px)
  `sizeY`: hauteur (px)
  `color`:(string) la couleur
  La tortue `tortue` est initialisée.
  post: un resctange de `sizeX` x `sizeY` en la couleur `color`
  """
  tortue.color(color)
  tortue.pendown()
  tortue.begin_fill()
  for i in range(2,6):
      tortue.forward(sizeX if i%2==0 else sizeY)
      tortue.right(90)
  tortue.end_fill()
  tortue.penup()
  tortue.forward(sizeX)
def three_color_flag(color1,color2,color3,width):
  """Dessine un drapeau vertical (comme celui de la belgique) de largeur `width` (et de proportion 3/2)
  les bandes auront respectivement
  `color1`,`color2`,`color3`

  pre:
  `width`: la largeur (px)
  `color1`:(string) la couleur 1
  `color1`:(string) la couleur 2
  `color1`:(string) la couleur 3
  La tortue `tortue` est initialisée.
  post: un drapeau verticale de largeur `width`et de couleurs: color1 color2 color3
  """
  colors = [color1,color2,color3]
  sizeX = width / 3 #largeur de chaque bande
  sizeY = width *1/2 #hauteur de chaque bande ration de de 3/2 (width * 3/2 / 3 )
  for color in [color1,color2,color3]:
    rectangle(sizeX,sizeY,color)
    tortue.penup()
def three_color_landscape_flag(color1,color2,color3,width):
  """Dessine un drapeau horizontale (comme celui du luxembourgh) de largeur `width` (et de proportion 3/2)
  les bandes auront respectivement
  `color1`,`color2`,`color3`

  pre:
  `width`: la largeur (px)
  `color1`:(string) la couleur 1
  `color1`:(string) la couleur 2
  `color1`:(string) la couleur 3
  La tortue `tortue` est initialisée.
  post: un drapeau horizontale de largeur `width`et de couleurs: color1 color2 color3
  """
  sizeX = width
  sizeY = (width *1/6)
  for color in  [color1,color2,color3]:
    rectangle(sizeX,sizeY,color)
    tortue.right(90)
    tortue.forward(sizeY)
    tortue.right(90)
    tortue.forward(sizeX)
    tortue.left(180)
  tortue.forward(sizeX)
  tortue.seth(90)
  tortue.forward(sizeY*3)
  tortue.right(90)
    # tortue.forward(sizeX)

def belgian_flag(width):
  """Dessine le drapeau belge de largeur `width`

  pre:
  `width`: la largeur (px)
  La tortue `tortue` est initialisée.
  post: le drapeau belge
  """
  three_color_flag("black","yellow","red",width)
def french_flag_flag(width):
  """Dessine le drapeau francais de largeur `width`

  pre:
  `width`: la largeur (px)
  La tortue `tortue` est initialisée.
  post: le drapeau francais
  """
  three_color_flag("blue","white","red",width)
def dutch_flag(width):
  """Dessine le drapeau des pays-bas de largeur `width`

  pre:
  `width`: la largeur (px)
  La tortue `tortue` est initialisée.
  post: le drapeau des pays-bas
  """
  three_color_landscape_flag("red","white","blue",width)
def german_flag(width):
  """Dessine le drapeau allemand de largeur `width`
  pre:
  `width`: la largeur (px)
  La tortue `tortue` est initialisée.
  post: le drapeau allemand
  """
  three_color_landscape_flag("black","red","yellow",width)
def luxemburg_flag_flag(width):
  """Dessine le drapeau luxembourgeois de largeur `width`

  pre:
  `width`: la largeur (px)
  La tortue `tortue` est initialisée.
  post: le drapeau du luxembourgh
  """
  three_color_landscape_flag("red","white","cyan",width)
def european_flag(width):
  """Dessine le drapeau europeen de largeur `width`

  pre:
  `width`: la largeur (px)
  La tortue `tortue` est initialisée.
  post: le drapeau europeen
  """
  width = width
  height = width * 2/3
  rayon = height*0.4
  starSize = height/12
  rectangle(width,height,"blue")
  #on se met tranquillou au centre
  tortue.right(90)
  tortue.forward(height/2)
  tortue.right(90)
  tortue.forward(width/2)
  tortue.left(180)
  for angle in range(0,360,360//12):
    tortue.left(angle)
    tortue.forward(rayon)
    tortue.right(angle)
    star(20)
    tortue.left(angle)
    tortue.backward(rayon)
    tortue.right(angle)


resetTopLeft()
belgian_flag(300)
margin_x(100)
french_flag_flag(300)
margin_x(100)
dutch_flag(300)
margin_x(100)
german_flag(300)
margin_x(100)
luxemburg_flag_flag(300)
resetTopLeft()
margin_y(350)
margin_x((turtle.window_width()//2)-450)
european_flag(900)
margin_x(-900*2/3)
margin_y(350)

tortue.right(45)
belgian_flag(300)
tortue.left(45)
margin_x(250)
belgian_flag(300)
margin_x(250)
tortue.left(45)
belgian_flag(300)
input("q")
