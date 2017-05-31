#!/usr/bin/env python2
"""Calculates how much money you have

assets-minus-liabilities.py calculates how much money you have on hand by
subtracting the amount of money in your assets accounts... by the amount
of money in your liabilities accounts.
"""

import gnucash
from datetime import date
from collections import OrderedDict

__author__ = "relyt29"
__copyright__ = "Copyright 2016, relyt29"
__credits__ = ["relyt29"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "relyt29"
__email__ = "f41c0r@hack.ink"
__status__ = "Production"


if __name__ == "__main__":

    session = gnucash.Session("/path/to/accounts.gnucash")
    book = session.get_book()
    rootAcc = book.get_root_account()
    assetsAcc = rootAcc.lookup_by_name("Assets")
    liabilitiesAcc = rootAcc.lookup_by_name("Liabilities")

    sumAssets = assetsAcc.GetBalance().to_double()
    print("Assets (Root Account): ".ljust(32) + str(sumAssets).rjust(12))
    assetsList = assetsAcc.get_descendants()
    for descendant in assetsList:
        print((descendant.name + ": ").ljust(32) + str(descendant.GetBalance()).rjust(12))
        sumAssets = descendant.GetBalance().to_double()
    
    print

    sumLiabilities = liabilitiesAcc.GetBalance().to_double()
    print("Liabilities (Root Account): ".ljust(32) + str(sumLiabilities).rjust(12))
    liabilitiesList = liabilitiesAcc.get_descendants()
    for descendant in liabilitiesList:
        print((descendant.name + ": ").ljust(32) + str(descendant.GetBalance()).rjust(12))
        sumLiabilities += descendant.GetBalance().to_double()

    print
    print
    print("Sum Total Assets:".ljust(32) + str(sumAssets).rjust(12))
    print("Sum Total Liabilities:".ljust(32) + str(abs(sumLiabilities)).rjust(12))
    print("Net Money on Hand".ljust(32) + str(sumAssets - abs(sumLiabilities)).rjust(12))

    session.end()
