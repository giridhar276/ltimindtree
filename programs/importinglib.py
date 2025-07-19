
##################### importing libraries ##################

# method1 : importing all the methods
import math
print(math.log(2))
print(math.tan(1))


# method2 : importing with alias name
import math as m
print(m.cos(1))
print(m.floor(34.1))

#method3 : importing required methods only
from math import log,cos
print(log(2))
print(cos(1))
