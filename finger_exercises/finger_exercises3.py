import pandas as pd, numpy, matplotlib

#write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message to that effect.

entered = int(input('Enter an integer: '))
root = 0
pwr = 0
for i in range(1,6):
  if root**pwr == entered:
    break
  pwr = i
  for r in range(1,entered):
    if root**pwr == entered:
      print('Root is:', str(root) + '.', 'Power is:', str(pwr) + '.')
      break
    else:
      root = r
if root**pwr != entered:
  print('No such pair of integers exist.')
