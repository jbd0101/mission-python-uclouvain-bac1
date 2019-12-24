"""
developpe par jean-christophe bauduin, groupe 11.13
"""

from mission8 import *

def testDuree():
  duree = Duree(2,12,4) #2h 12min 4s
  ds = 2*60*60+12*60+4
  assert duree.toSecondes()==ds
  assert duree.delta(4)== ds-4
  assert not duree.apres(ds-10)
  assert duree.apres(ds+10)
  assert str(duree)=="02:12:04"
  duree.ajouter(90)
  assert str(duree)== "02:13:34"
  try:
    Duree(4,-4,0)
  except Exception as e:
    pass
  else:
    raise AssertionError
  try:
    Duree(4,4,-10)
  except Exception as e:
    pass
  else:
    raise AssertionError

def test_chanson():
  chanson = Chanson("test","jc",Duree(0,0,40))
  assert str(chanson)=="test - jc - 00:00:40"
def testAlbum():
  album = Album()
  chanson = Chanson("test","jc",Duree(0,0,60))
  assert album.duree() == 0
  assert album.length() == 0
  album.add(chanson)
  assert album.duree() == 60
  assert album.length() == 1
  for i in range(73):
    a = album.add(chanson)
    assert a
  assert not album.add(chanson)
testDuree()
test_chanson()
testAlbum()
