import pandas as pd, numpy, matplotlib

# What would have to be changed to make the code in Figure 3.4 work for finding an approximation to the cube root of both negative and positive numbers? (Hing: think about changing low to ensure that the answer lies within the region being searched.)

x = -27
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (high + low)/2.0
while abs(ans**3 - abs(x)) >= epsilon:
  print ('low =', low, 'high =', high, 'ans =', ans)
  numGuesses += 1
  if ans**3 < abs(x):
    low = ans
  else:
    high = ans
  ans = (high + low)/2.0
if x < 0:
  ans *= -1
  print('x is negative')  
print('numGuesses =', numGuesses)
print(ans, 'is close to the square root of', x)