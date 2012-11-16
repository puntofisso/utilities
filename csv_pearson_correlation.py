import csv
from itertools import imap
import math

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

def main():
    ident = []
    x = []
    y = []
    filename='Extract.csv'

    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar="|")
        for row in spamreader:
           ident.append(row[0])
           x.append(int(row[1]))
           y.append(int(row[2]))
        print "Calculating Pearson Correlation..."
        print str(pearson_def(x, y))

main()
