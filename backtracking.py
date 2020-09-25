# F: R->R
# Backtracking line search

# @param
# f:    object function
# d_f:  derivative function of object
# x:    value of variable to compute
# d_x:  descent direction
# alpha,beta: parameter to compute step size
def backtracking(f,d_f,x,d_x,alpha=0.1,beta=0.6):
    # initial guess of t
    t = 1.
    # trying different t and decrease over the iterations
    while f( x + t*d_x ) > f(x) + alpha*t*d_f(x)*d_x:
        #print "trying step size ", t
        t = beta*t
        # print "final step size ", t
    return t