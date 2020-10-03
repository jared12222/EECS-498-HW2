from SGDtest import fi,fiprime,maxi,fsum
import matplotlib.pyplot as plt
from sgd import sgd

def main():
    x = sgd(fi,fiprime,x0=-5,i_range = maxi,t=1,iteration = 1000)
    print "sgd complete"
    f = []
    print "Plotting, may take a while"
    for n in x:
        f.append(fsum(n))
    
    plt.plot(f)
    plt.xlabel("Number of iterations(i)")
    plt.ylabel("fsum(x_i)")
    plt.show()
    

if __name__ == "__main__":
    main()