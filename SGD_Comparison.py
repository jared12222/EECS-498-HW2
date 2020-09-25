# Compare mean and var results from SGD between 1000 and 750 iterations with 30 times each

from SGDtest import fi,fiprime,maxi,fsum
import matplotlib.pyplot as plt
from sgd import sgd
import numpy as np

def main():
    x_750 = []
    x_1000 = []
    for i in range(0,30):
        x_750.append(sgd(fi,fiprime,x0=-5,i_range = maxi,t=1,iteration = 750))
        x_1000.append(sgd(fi,fiprime,x0=-5,i_range = maxi,t=1,iteration = 1000))
    x_750 = np.matrix(x_750)
    x_1000 = np.matrix(x_1000)
    print "sgd complete"
    print "750  iterations and 30 times, mean = %.5f, var = %.5f" % (np.mean(x_750[...,-1]),np.var(x_750[...,-1]))
    print "1000 iterations and 30 times, mean = %.5f, var = %.5f" % (np.mean(x_1000[...,-1]),np.var(x_1000[...,-1]))
if __name__ == "__main__":
    main()