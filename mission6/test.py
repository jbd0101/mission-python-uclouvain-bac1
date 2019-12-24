#dev par Jean christophe bauduin et timour petit
import assistant
def testSum():
  assert ("10" in assistant.dispatch("sum 5 5"))
def testAvg():
  assert ("5" in assistant.dispatch("avg 5 5"))
def testFile():
  assert ("erreur" in assistant.dispatch("file sdfjkl"))
  # assert "charge" in assistant.dispatch("file all-words.dat")
testSum()
testAvg()
testFile()
