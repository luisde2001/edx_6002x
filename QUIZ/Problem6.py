def probTest(limit):
    n = 1
    while ((5 ** (n - 1)) / float(6 ** n)) > limit:
        n += 1
    return n

##print(probTest(.5))
##print(probTest(.14))
##print(probTest(.12))
##print(probTest(.1))
##print(probTest(.018))