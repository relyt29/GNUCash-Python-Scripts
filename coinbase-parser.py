#!/usr/bin/env python3
"""Calculates your mean buy in price from Coinbase.

This script parses a coinbase capital gains document to allow you to
figure out what your mean buy in price was - i.e. overall how much you
paid for eth per coin. It also displays what the sum of your purchases
was, and some other stats.
"""

import argparse
import csv
import requests

__author__ = "relyt29"
__copyright__ = "Copyright 2016, relyt29"
__credits__ = ["relyt29"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "relyt29"
__email__ = "f41c0r@hack.ink"
__status__ = "Production"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("coinbaseCSV", help="Path to exported coinbase CSV file for parsing.")
    args = parser.parse_args()

    runningTotal = 0.0
    amountCoin = 0.0
    with open(args.coinbaseCSV, "r") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        print(next(spamreader))
        print(next(spamreader))
        print(next(spamreader))
        print(next(spamreader))
        print(next(spamreader))
        print(next(spamreader))
        print(next(spamreader))
        print(next(spamreader))
        print(next(spamreader))
        print(next(spamreader))
        print(next(spamreader))
        print(next(spamreader))
        print()
        print("TRANSACTION LIST:")
        print("="*44)

        for row in spamreader:
            try:
                paid = float(row[4])
                costPerCoin = float(row[3])
                amountCoin += paid / costPerCoin
                runningTotal += paid
                row2 = [row[3], row[4]]
                print("{: >10} {: >10}".format(*row2))
            except IndexError:
                continue


    print()
    print("NET SUMS:")
    print("="*44)
    print("Sum Total:                 {0:.2f}".format(runningTotal))
    print("Amount Coin:               {0:.5f}".format(amountCoin))
    meanCost = runningTotal / amountCoin
    print("Mean Cost per Coin:        {0:.2f}".format(meanCost))

    headers = {'CB-VERSION': '2017-05-31'}
    resp = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/spot', headers=headers)
    currentCost = float(resp.json()['data']['amount'])
    print("Current Cost per Coin:     {0:.2f}".format(currentCost))
    print("Value of Current Holdings: {0:.2f}".format(currentCost * amountCoin))
    print("Percent Gains:             {0:.2f}%".format(
        (currentCost / meanCost) * 100.00)
    )

