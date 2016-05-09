'''
# Paste your code into this box
balance = 3329
annualInterestRate = 0.2
Month = 0
TotalPaid = 0
OldBalance = balance
MinimumPayment = balance * annualInterestRate

while Month != 12:
    Month += 1
    UnpaidBalance = balance - MinimumPayment
    Interest = (annualInterestRate / 12) * UnpaidBalance
    balance = UnpaidBalance + Interest
    TotalPaid = TotalPaid + MinimumPayment
    print str("Month: ") +  str(Month)
    print str("Minimum monthly payment: ") +  str("%.2f" % MinimumPayment)
    print str("Remaining balance: ") + str("%.2f" % balance)


print str("Total paid: ") + str("%.2f" % TotalPaid)
print str("Remaining balance: ") + str("%.2f" % balance)
'''
balance = 4773
annualInterestRate = 0.2
bal = balance
miniPay=0
while bal>0:
    miniPay+=10
    print miniPay
    bal = balance
    for i in range(12):
        print bal
        print 'Mounth' + str(i)
        unPaidBal = bal-miniPay
        print unPaidBal
        bal = unPaidBal+unPaidBal*(annualInterestRate/12)
        print bal

print "Lowest Payment: " + str(miniPay)