import pandas as pd
import numpy
import matplotlib
print(matplotlib.__version__)
print(pd.__version__)
print (numpy.__version__)

# Asks the user to enter a number “x”
x = float(input('Please pick a number for x.\n'))
# Asks the user to enter a number “y”
y = float(input('Please pick a number for y.\n'))

# Prints out number “x”, raised to the power “y”.
print('x**y=',x**y)

# Prints out the log (base 2) of “x”. 
print('log(x)=',numpy.log(x))