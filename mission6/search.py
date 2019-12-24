file = ""
import re
with open("test.txt","r") as f:
  file = f.read()
  file = sorted(re.split("[\s]",file)) #le split par regex est FACULTATIF , mais tres utilie pour le dictionnaire avec numeros...
def binary_search ( name, list_of_names ):
  first = 0
  last = len(list_of_names)-1
  found = False

  while first<=last and not found:
    middle = (first + last)//2
    if list_of_names[middle] == name:
      found = True

    else:
      if name < list_of_names[middle]:
        last = middle-1
      else:
        first = middle+1
  return list_of_names[(first+last)//2]
print(binary_search("shelling",file))
