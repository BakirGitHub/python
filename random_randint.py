def najveciElement(niz):
  najveci=niz[0]
  for i in range(1,len(niz)):
    if niz[i]> najveci:
      najveci = niz[i]
  return najveci

def brojPojavljivanja(niz,element):
  brojac=0
  for i in range(len(niz)):
    if element==i:
      brojac+=1
  return brojac

def brojpojavljivanjaNajveceg(niz):
  return brojPojavljivanja(najveciElement(niz))




