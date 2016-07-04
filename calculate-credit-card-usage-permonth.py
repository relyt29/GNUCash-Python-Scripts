#!/usr/bin/env python2

import gnucash
from datetime import date
from collections import OrderedDict

session = gnucash.Session("/path/to/accounts.gnucash")
book = session.get_book()
rootAcc = book.get_root_account()
creditCard = rootAcc.lookup_by_name("Name of Credit Card Account in GNUCash")

splitList = creditCard.GetSplitList()

rollingSumSpent = 0.00
rollingSumPaidDown = 0.00
perMonthDict = OrderedDict()
rollingAverage = 0.00

for splitItem in splitList:
    splitAmount = float( str( splitItem.GetAmount() ) )
    trans = splitItem.GetParent()
    transDate = date.fromtimestamp(trans.GetDate())
    if splitAmount < 0:
        rollingSumSpent += splitAmount
    else:
        rollingSumPaidDown += splitAmount

    dateDictKey = (str(transDate.month),str(transDate.year))
    if splitAmount < 0:
        rollingAverage = perMonthDict.get(dateDictKey)

        if rollingAverage != None:
            rollingAverage += splitAmount
        else:
            rollingAverage = splitAmount

        perMonthDict[dateDictKey] = rollingAverage


print "Total Spent on Card: " + str(rollingSumSpent)
print "Total Paid Down on Card: " + str(rollingSumPaidDown)
print "Per month Spending:" 
print
for m in perMonthDict:
    print m[0] + "/" + m[1] + " " + str(abs(perMonthDict[m]))
print
numMonths = len(perMonthDict)
if numMonths == 0: # Divide by 0 BS
    numMonths = 1
print "Mean Average per Month: " + str( abs(rollingSumSpent) / numMonths )

session.end()
