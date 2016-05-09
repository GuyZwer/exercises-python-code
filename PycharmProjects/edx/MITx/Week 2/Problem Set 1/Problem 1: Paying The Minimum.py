balance = 5000
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

Month = 0
TotalPaid = 0
OldBalance = balance

while (Month != 12):
    Month += 1
    MinimumPayment = balance * monthlyPaymentRate
    UnpaidBalance = balance - MinimumPayment
    Interest = (annualInterestRate / 12) * UnpaidBalance
    balance = UnpaidBalance + Interest
    TotalPaid = TotalPaid + MinimumPayment
    print str("Month: ") +  str(Month)
    print str("Minimum monthly payment: ") +  str("%.2f" % MinimumPayment)
    print str("Remaining balance: ") + str("%.2f" % balance)


print str("Total paid: ") + str("%.2f" % TotalPaid)
print str("Remaining balance: ") + str("%.2f" % balance)

