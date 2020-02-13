import pandas as pd
import numpy
import matplotlib
print(matplotlib.__version__)
print(pd.__version__)
print (numpy.__version__)

#Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered. If no odd number was entered, it should print a message to that effect.

#ask user to input a, b, c, d, e, f, g, h, i and j and change input to an int

a = int(input('Please pick a number for a.\n'))
b = int(input('Please pick a number for b.\n'))
c = int(input('Please pick a number for c.\n'))
d = int(input('Please pick a number for d.\n'))
e = int(input('Please pick a number for e.\n'))
f = int(input('Please pick a number for f.\n'))
g = int(input('Please pick a number for g.\n'))
h = int(input('Please pick a number for h.\n'))
i = int(input('Please pick a number for i.\n'))
j = int(input('Please pick a number for j.\n'))

#determine which ints are odd

if a%2 == 0:
  a = 0
pass

if b%2 == 0:
  b = 0
pass

if c%2 == 0:
  c = 0
pass

if d%2 == 0:
  d = 0
pass

if e%2 == 0:
  e = 0
pass

if f%2 == 0:
  f = 0
pass

if g%2 == 0:
  g = 0
pass

if h%2 == 0:
  h = 0
pass

if i%2 == 0:
  i = 0
pass

if j%2 == 0:
  j = 0
pass

print(a, b, c, d, e, f, g, h, i, j)

#determine which int is largest
value = a, b, c, d, e, f, g, h, i, j
largest_odd = int(max(value))

if largest_odd == 0:
  print('There are no odd numbers.')
else:
  print('The largest odd number is ' + str(largest_odd) + '.')

