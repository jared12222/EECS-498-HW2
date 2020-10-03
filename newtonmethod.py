## Something wrong with my newton

def NewtonMethod(f,d_f,dd_f,x0,epson = 0.0001):
    from backtracking import backtracking
    x = [x0]

    while True:
        df = d_f(x[-1])
        ddf = dd_f(x[-1])
        if (df**2/ddf)/2 <= epson:
            break
        d_x = -df/ddf
        t = backtracking(f,d_f,x[-1],d_x)
        x.append(x[-1] + t*d_x)
    #     print "%3.3f,%.3f,%.3f" % (d_x,t,x[-1])
    # print "Final x: %.3f" % (x[-1])
    return x

def f(x):
    return x**2
def d_f(x):
    return 2*x
def dd_f(x):
    return 2

if __name__ == "__main__":
    print "Running gradientdescent"

    print NewtonMethod(f,d_f,dd_f,10)