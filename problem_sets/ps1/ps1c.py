import pandas as pd
import numpy
import matplotlib
print(matplotlib.__version__)
print(pd.__version__)
print (numpy.__version__)

#Find the savings rate needed to save the down payment in the time period
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
down_payment = 0.25 * total_cost
months = 36
current_savings = 0

base_annual_salary = float(input('Please enter your annual salary.\n'))

maximum = 10000                   #100% of salary
epsilon = 100                     #acceptable margin of error
guesses = 0
low = 0                           #0% of salary
high = max(1, maximum)
portion_saved = (high + low) / 2  #initial guess

while abs(current_savings - down_payment) >= epsilon:
  print ('low = ', low, 'high = ', high, 'portion_saved = ', portion_saved)
  guesses = guesses + 1
  current_savings = 0.0                     #restart with updated guess
  annual_salary = base_annual_salary        #restart with updated guess
  for month in range(1, months + 1):
    current_savings = current_savings + current_savings*r/12 + (annual_salary / 12 * portion_saved / 10000)
    if month % 6 == 0:
      annual_salary = annual_salary*(1 + semi_annual_raise)
  prev_portion_saved = portion_saved
  if current_savings > down_payment:
    high = portion_saved
  else:
    low = portion_saved
  portion_saved = int(round((high + low) / 2))
  if prev_portion_saved == portion_saved:
    break

if prev_portion_saved == portion_saved and portion_saved == maximum:
  print('It is not possible to save the down payment in three years.')
else:
  print('Steps = ', guesses)
  portion_saved = portion_saved / 10000
  print('Best savings rate: ', portion_saved)



