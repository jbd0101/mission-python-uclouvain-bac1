#dev par Jean-Christophe Bauduin et Aurian Begon
#le 6/11
import search
def test_open_ex1():
  file = open("test_example_1.txt","r")
  f = file.read()
  file.close()
  assert search.readfile("test_example_1.txt") == f
def test_open_ex2():
  file = open("test_example_2.txt","r")
  f = file.read()
  file.close()
  assert search.readfile("test_example_2.txt") == f

def test_cleanup():
  txt = "BoNJO.??'Ur!"
  assert search.cleanup(txt)=="bonjour"
def test_get_words():
  line = "sal!ut bonjOur"
  assert search.get_words(line) == ["salut","bonjour"]
def test_get_lines():
  index = search.create_index("test_example_2.txt")
  words = ["the","republic"]
  assert search.get_lines(words,index)==[261, 282]
test_open_ex1()
test_open_ex2()
test_cleanup()
test_get_words()
test_get_lines()

