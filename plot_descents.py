from math import exp
import matplotlib.pyplot as plt
import numpy
def f(x):
    try:
        # If x is iteratible, return result in list form
        y = []
        for i in x:
            y.append(exp(0.5*i+1)+exp(-0.5*i-0.5)+5*i)
    except Exception:
        y = exp(0.5*x+1)+exp(-0.5*x-0.5)+5*x
    return y
def d_f(x):
    try:
        # If x is iteratible, return result in list form
        y = []
        for i in x:
            y.append(0.5*exp(0.5*i+1)-0.5*exp(-0.5*i-0.5)+5)
    except Exception:
        y = 0.5*exp(0.5*x+1)-0.5*exp(-0.5*x-0.5)+5
    return y
def dd_f(x):
    try:
        # If x is iteratible, return result in list form
        y = []
        for i in x:
            y.append(0.25*exp(0.5*i+1)+0.25*exp(-0.5*i-0.5))
    except Exception:
        y = 0.25*exp(0.5*x+1)+0.25*exp(-0.5*x-0.5)
    return y


def main():
    x0 = 5
    from newtonmethod import NewtonMethod
    from gradientdescent import GradientDescent
    x_new = NewtonMethod(f,d_f,dd_f,x0)
    y_new = f(x_new)
    x_gd  = GradientDescent(f,d_f,x0)
    y_gd  = f(x_gd)
    x = [ x for x in numpy.arange(-10,10,0.1)]
    y = f(x)
    print(x_new)
    print(x_gd)
    # plt.subplot(211)
    plt.plot(x,y,'k',label="Objective")
    plt.plot(x_new,y_new,'mx-',label="Newton Method")
    plt.plot(x_gd,y_gd,'ro-',label = "Gradient Descent")
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.xlim([-10,10])
    plt.title('Newton versus GD - x,f(x)')
    plt.savefig("prob1d_i.png")
    plt.show()
    # plt.subplot(212)
    plt.plot(y_new,'mx-',label="Newton",linewidth=3.0)
    plt.plot(y_gd,'ro-',label="Gradient Descent")
    plt.xlabel('Number of Iterations i')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Newton versus GD - f(x_k)')
    plt.savefig("prob1d_ii.png")
    plt.show()

if  __name__ == "__main__":
    main()