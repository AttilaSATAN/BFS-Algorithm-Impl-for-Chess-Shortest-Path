import math

moves = [[-2, -1], [-2, +1], [-1, -2], [-1, +2], [+2, +1], [+2, -1], [+1, +2], [+1, -2]]
mark = []
que = []


def toVect(number):
  y = int(math.floor(number/8))
  x = number%8
  return x, y

# vektorel koordinatları sayısal koordinata çeviralim
def toOrder(vect):
  return vect[1] * 8 + vect[0]

# koordinatların tahtanın içinde olduğuna emin olalım
def validate(move, x, y):
  nX = move[0] + x
  nY = move[1] + y
  
  if str(nX) + '-' + str(nY) in mark:
    return False
  
  return 0 < nX < 7 and 0 < nY < 7

def bfs(src, dest):
  srcC = toVect(src)
  destC = toVect(dest)
  
def moveTry(stepNum, stepSrc, destC):
  while 
# BFS ile çözüm
bfs(4,4)
