import math


moves = [[-2, -1], [-2, +1], [-1, -2], [-1, +2], [+2, +1], [+2, -1], [+1, +2], [+1, -2]]
mark = []
que = []

def marker(x, y):
  mark.append(str(x) + '-' + str(y))
# Numaralandirilmis hucreler yerine koordinat sistemi kullanmak sinir tespiti ve klasik algoritmalar kullanmayi kolaylastirir.
def toVect(cellNumber):
  y = int(math.floor(cellNumber/8))
  x = cellNumber%8
  return x, y

# vektorel koordinatlari sayisal koordinata cevirelim
def toOrder(vect):
  return vect[1] * 8 + vect[0]

# koordinatlarin tahtanin icinde olduguna emin olalim
def validate(move, x, y):
  nX = move[0] + x
  nY = move[1] + y
  
  if str(nX) + '-' + str(nY) in mark:
    return False
  
  if -1 < nX < 8 and -1 < nY < 8:
    marker(nX, nY)
    return True
  return False

def answer(src, dest):
  
  srcC = list(toVect(src))
  srcC.append(0)
  # baslangic noktasini isaretleyelim
  marker(srcC[0], srcC[1])
  destC = list(toVect(dest))

  #baslangic noktasini kontrol sirasina ekleyelim
  que.append(srcC)

  while len(que) > 0:
    
    d = que.pop(0)
    print(d[0], d[1], d[2])
    if d[0] == destC[0] and d[1] == destC[1]:
      print('HIT ', d[2])
      return d[2]

    for m in moves:

      x = m[0] + d[0]
      y = m[1] + d[1]
      n = d[2] + 1
      if validate(m, d[0], d[1]):
        marker(x,y)
        que.append([x,y,n])
  print('What now?', mark)

answer(1,60)
