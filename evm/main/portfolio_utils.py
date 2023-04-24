# portfolio_utils.py
import wget
import random
import csv
from os import system

def read_portfolio_file(url):
    print("\n")
    portfolio = "/tmp/portfolio_" + str(random.randint(1, 100000)) + ".csv"
    response = wget.download(url, portfolio)
    # print("\n Portfolio File Name ==>", portfolio)
    # system("cat " + portfolio)
    print("\n")
    file = open(portfolio)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
        # print(row)
    # print(header)
    # print(rows)
    file.close()
    return portfolio, header, rows

