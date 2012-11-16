import csv
from itertools import imap
import math
from scipy.stats.stats import pearsonr


#Correlation 	Negative 	Positive
#None 		-0.09 to 0.0 	0.0 to 0.09
#Small 		-0.3 to -0.1 	0.1 to 0.3
#Medium 	-0.5 to -0.3 	0.3 to 0.5
#Strong 	-1.0 to -0.5 	0.5 to 1.0

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
        print "Calculating Pearson Correlation manually..."
        res = pearson_def(x, y)
        print res

        if (res > 0.5):
            print "STRONG (POSITIVE)"
        elif (res > 0.3):
            print "MEDIUM (POSITIVE)"
        elif (res > 0.1):
            print "SMALL (POSITIVE)"
        elif (res > 0):
            print "NONE (POSITIVE)"
        elif (res > 0.1):
            print "NONE (NEGATIVE)"
        elif (res > 0.3):
            print "SMALL (NEGATIVE)" 
        elif (res > 0.5):
            print "MEDIUM (NEGATIVE)"
        elif (res > -1.0):
            print "STRONG (NEGATIVE)"
           

        print "Calculating Pearson Correlation with scipy..."
        res = pearsonr(x, y)
        print res[0]

main()
