__author__ = 'ryan@barnett.io'
'''Write a program that uses bisection search (for more info check out the Wikipedia page on bisection
 search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay
 off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large
 inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.'''

balance = 999999
currentBalance = balance
annual_interest_rate = .18
monthly_interest_rate = annual_interest_rate / 12.0
monthly_lower_bound = currentBalance / 12
monthly_upper_bound = currentBalance * ((1 + monthly_interest_rate) ** 12) / 12.0
months = 0
epsilon = .001
guess = (monthly_upper_bound + monthly_lower_bound)/2.0

while balance >= epsilon:
    months += 1
    currentBalance -= guess
    currentBalance += currentBalance*(monthly_interest_rate)
    if months == 12 and currentBalance >= 0 and currentBalance <= epsilon:
        balance = currentBalance
        print "Lowest Payment:", guess
        print currentBalance
    elif months == 12 and currentBalance > epsilon:
        months = 0
        currentBalance = balance
        monthly_lower_bound = guess
        print('lower bound = ' + str(monthly_lower_bound) + '\nupper bound = ' + str(monthly_upper_bound))
        print 'guess is too low'
    elif months == 12 and currentBalance < epsilon:
        months = 0
        currentBalance = balance
        monthly_upper_bound = guess
        print('lower bound = ' + str(monthly_lower_bound) + '\nupper bound = ' + str(monthly_upper_bound))
        print 'guess is too high'
    guess = (monthly_upper_bound + monthly_lower_bound)/2.0


