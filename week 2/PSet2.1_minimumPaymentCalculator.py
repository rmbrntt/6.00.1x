__author__ = 'ryan@barnett.io'
'''Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
 required by the credit card company each month.'''

balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04
months = 12
monthlyInterestRate = annualInterestRate/months
currentBalance = 0
totalPaid = 0
for month in range(months):
    monthlyPayment = balance*monthlyPaymentRate
    currentBalance = balance-monthlyPayment
    balance = currentBalance+(monthlyInterestRate*currentBalance)
    totalPaid += monthlyPayment
    print "Month:", month+1
    print "Minimum monthly payment:", round(monthlyPayment, 2)
    print "Remaining balance:", round(balance, 2)
print "Total paid:", round(totalPaid, 2)
print "Remaining balance:", round(balance, 2)