__author__ = 'ryan@barnett.io'
'''Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance
within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is
a constant amount that will be paid each month.'''

balance = 3926
annualInterestRate = .2
months = 12
increment = 10
currentBalance = balance
while balance >= 0:
    currentBalance -= increment
    currentBalance += currentBalance*(annualInterestRate/12)
    months -= 1
    if months == 0 and currentBalance <= 0:
        balance = currentBalance
        print "Lowest Payment:", increment
    elif months == 0 and currentBalance > 0:
        months = 12
        currentBalance = balance
        increment += 10

################ did not meet use case
# while months >= 1:
#     fixedPayment = balance/months
#     monthlyPayment = fixedPayment+(monthlyInterestRate*balance)
#     currentBalance = balance-monthlyPayment
#     balance = currentBalance
#     totalPaid += monthlyPayment
#     print "Month:", months
#     print "Minimum monthly payment:", round(monthlyPayment, 2)
#     print "Remaining balance:", round(balance, 2)
#     months -= 1
# print "Total paid:", round(totalPaid, 2)
# print "Remaining balance:", round(balance, 2)






