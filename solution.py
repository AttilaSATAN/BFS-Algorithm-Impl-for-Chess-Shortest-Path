
import math
### Use this space to try out ideas and free code ###
def coordinat(number):
  y = int(math.floor(number/8))
  x = number%8
  return x, y

def answer(src, dest):
  srcC = coordinat(src)
  destC = coordinat(dest)
  
  doubleStepCount = [0,0]
  singleStepCount = [0,0]
  
  for i in range(2):
    
    singleStepCount[i] = 0
    r = srcC[i] - destC[i]
    if r % 2 == 1:
      doubleStepCount[i] = int(math.floor(r / 2))
      singleStepCount[i] = 1
    else: 
      doubleStepCount[i] = int(r / 2)
  
  print(doubleStepCount)
  print(singleStepCount)

# -2, -1
# -2, +1
# -1, -2
# -1, +2
# +2, +1
# +2, -1
# +1, +2
# +1, -2


answer(34,7)
    
