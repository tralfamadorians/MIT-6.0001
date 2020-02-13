import pandas as pd
import numpy
import matplotlib
print(matplotlib.__version__)
print(pd.__version__)
print (numpy.__version__)

# to find = percent_saved
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
down_payment = 0.25 * total_cost

annual_salary = float(input('Please enter your annual salary.\n'))
months = float(input('Please enter the number of months you would like to take to reach your goal.\n'))

tmp_months = 0
while tmp_months < months:
  xxx
  tmp_months = tmp_months + 1
  if months%6 == 0:
    annual_salary = annual_salary * (1 + semi_annual_rate)
  pass  


portion_saved = percent_saved * 100   #change from decimal to %
print()
print('Savings rate: ' + str(percent_saved) + %)

#ps1b solution
months = 0
while current_savings <= cash_needed:
  current_savings = current_savings + current_savings*r/12 + (annual_salary / 12 * portion_saved)
  months = months + 1
  if months%6 == 0:
    annual_salary = annual_salary*(1 + semi_annual_raise)
  pass 
