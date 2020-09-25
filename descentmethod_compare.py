# Compare SGD, GD,Newton with 1000 iterations on SGD

from SGDtest import fi,fiprime,fiprimeprime,maxi,fsum,fsumprime,fsumprimeprime
import matplotlib.pyplot as plt
from sgd import sgd
from gradientdescent import GradientDescent
from newtonmethod import NewtonMethod
import numpy as np
import time

def main():
    start = time.clock()
    x_SGD = sgd(fi,fiprime,x0=-5,i_range = maxi,t=1,iteration = 1000)
    end   = time.clock()
    print "SGD    time: %f" % (end-start)
    print "fsum       = %f" % (fsum(x_SGD[-1]))

    start = time.clock()
    x_GD  = GradientDescent(fsum,fsumprime,-5,epson=0.0001)
    end   = time.clock()
    print "GD     time: %f" % (end-start)
    print "fsum       = %f" % (fsum(x_GD[-1]))

    start = time.clock()
    x_new = NewtonMethod(fsum,fsumprime,fsumprimeprime,-5,epson=0.0001)
    end   = time.clock()
    print "Newton time: %f" % (end-start)
    print "fsum       = %f" % (fsum(x_new[-1]))
    
    plt.subplot(311)
    plt.plot(x_SGD,'r')
    plt.subplot(312)
    plt.plot(x_GD,'b')
    plt.subplot(313)
    plt.plot(x_new,'m')
    plt.show()

if __name__ == "__main__":
    main()