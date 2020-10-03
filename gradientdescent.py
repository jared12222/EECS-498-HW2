#! /usr/bin/env python
# Gradient Descent Method
# @param
# f:     objective function
# d_f:   derivative of objective function
# x0:    initial guess of x
# epson: termination condition
def GradientDescent(f,d_f,x0,epson = 0.0001):
    from backtracking import backtracking
    x = [x0]
    
    while True:
        # determine d_x
        d_x = -d_f(x[-1])
        if d_x**2 <= epson:
            break
        t = backtracking(f,d_f,x[-1],d_x)
        x.append(x[-1] + t*d_x)
    #     print "%3.3f,%.3f,%.3f" % (d_x,t,x[-1])
    # print "Final x: ",x[-1]
    return x

def f(x):
    return x**2
def d_f(x):
    return 2*x

if __name__ == "__main__":
    print "Running gradientdescent"

    print GradientDescent(f,d_f,10.)
    
    