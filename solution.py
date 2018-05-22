
import math
### Use this space to try out ideas and free code ###
def coordinat(number):
    y = int(math.floor(number/8))
    x = number%8
    return x, y

def answer(src, dest):
    print(coordinat(src))
    print(coordinat(dest))
    
# -2, -1
# -2, +1
# -1, -2
# -1, +2
# +2, +1
# +2, -1
# +1, +2
# +1, -2


answer(33,5)

