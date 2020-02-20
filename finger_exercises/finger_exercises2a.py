import pandas as pd
import numpy
import matplotlib
print(matplotlib.__version__)
print(pd.__version__)
print (numpy.__version__)

#Let s be a string that contains a sequence of decimal numbers separated by commas, e.g., s = '1.23,2.4,3.123.' Write a program that prints the sume of the numbers in s.

s = '1.1, 2.2, 3.3, 4.4'
print (s.split(',')) 
total = sum(map(float, s.split(',')))
print(total)