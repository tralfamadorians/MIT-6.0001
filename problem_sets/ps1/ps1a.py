import pandas as pd
import numpy
import matplotlib
print(matplotlib.__version__)
print(pd.__version__)
print (numpy.__version__)

#total_cost
portion_down_payment = 0.25
current_savings = 0
#annual return of savings = r
r = 0.04
# monthly savings growth = current_savings*r/12
#annual_salary
#salary saved = portion_saved
#monthly_salary

#Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats. Your program should ask the user to enter the following variables:
#1. The starting annual salary (annual_salary)
#2. The portion of salary to be saved (portion_saved)
#3. The cost of your dream home (total_cost)

annual_salary = float(input('Please enter your annual salary.\n'))
portion_saved = float(input('Please enter the percentage of your salary to be saved.\n'))
total_cost = float(input('Please enter the cost of your dream home.\n'))

#amount to be saved
cash_needed = total_cost * portion_down_payment

#convert x% saved into 0.x saved if necessary
if portion_saved > 1:
  portion_saved = portion_saved / 100
pass

#convert yearly amounts into monthly
monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * portion_saved

months = 0
while current_savings <= cash_needed:
  current_savings = current_savings + current_savings*r/12 + monthly_saved
  months = months + 1

print()
print('Number of months: ' + str(months))  


