import pandas as pd
import numpy
import matplotlib
print(matplotlib.__version__)
print(pd.__version__)
print (numpy.__version__)

#write a program that examines three variables--x, y and z-- and prints the largest odd number among them. If none of them are odd, it should print a message to that effect.

#ask user to input x, y and z and change input to an int

x = int(input('Please pick a number for x.\n'))
y = int(input('Please pick a number for y.\n'))
z = int(input('Please pick a number for z.\n'))


# This program exmamines variables x, y, and z 
# and prints the largest odd number among them

if x%2 != 0:
  if y%2 != 0:
    if z%2 != 0:
      if x > y and x > z: #x is the biggest odd
        print('x is the largest odd number')
      elif y > z and y > x: #y is the biggest odd
        print('y is the largest odd number')
      elif z > x and z > y: #z is the biggest odd
        print('z is the largest odd number')

    else: #z is even
      if x > y: #x is the biggest odd
        print('x is the largest odd number')
      else: #y is the biggest odd
        print('y is the largest odd number')

  else: #y is even
    if z%2 != 0: #z is odd
      if x > z: #x is the biggest odd
        print('x is the largest odd number')
      else: #z is the biggest odd
        print('z is the largest odd number')
    else: #y,z are even and x is the biggest odd
      print('x is the largest odd number')

else: #x is even
  if y%2 != 0 and z%2 != 0: #y,z is odd
    if y > z: #y is the biggest odd
      print('y is the largest odd number')
    else: #z is the biggest odd
      print('z is the largest odd number')
  else: #x and y is even
    if z%2 != 0: #z is the biggest odd
      print('z is the largest odd number')
    else:
      print('x, y and z are even numbers')



