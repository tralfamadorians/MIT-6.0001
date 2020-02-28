import pandas as pd, numpy, matplotlib

#Newton-Rephson for square root
#Find x such that x**2 - 24 is within epsilon of 0
#Finger exercise: Add some code to the implementation of Newton-Raphson that keeps track of the number of iterations used to find the root. Use that code as part of a program that compares the efficiency of Newton-Raphson and bisection search. (You should discover that Newton-Raphson is more efficient.)

#Newton-Raphson
epsilon = 0.01
k = 24.0
guess = k/2.0
num_Guesses = 0
while abs(guess*guess - k) >= epsilon:
  guess = guess - (((guess**2)-k)/(2*guess))
  num_Guesses += 1
print('Square root of', k, 'is about', guess)
print('Number is guesses with Newton-Raphson method is', num_Guesses)

#bisect search
x = 24
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (high + low)/2.0
while abs(ans**2 - abs(x)) >= epsilon:
  numGuesses += 1
  if ans**2 < abs(x):
    low = ans
  else:
    high = ans
  ans = (high + low)/2.0
if x < 0:
  ans = str(ans) + 'i'  
print('Number of guesses with bisect search is', numGuesses)
print(ans, 'is close to the square root of', x) 
