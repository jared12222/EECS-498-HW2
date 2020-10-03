import numpy
from cvxopt import matrix, solvers

def main():
    c = matrix([75.,128.,70.,34.])
    G = matrix([[ -1., 0., 0., 0., -1.6, -3.5,  -0.1, -2.3,  -6.1,],
                [  0.,-1., 0., 0., -7.2, -2.1,  -7.1, -3.2,  -0.1,],
                [  0., 0.,-1., 0., -3.7, -3.2,  -2.9, -3.4,  -4.9,],
                [  0., 0., 0.,-1., -0.1, -0.15, -0.1, -0.15, -0.1,]])
    h = matrix([   0., 0., 0., 0., -51., -48.,  -202.,-120., -229.,])
    
    sol = solvers.lp(c, G, h)
    print(sol['x'])

    robo_name = ["SpiderBot P8","Gigantimus Maximus","VersaDroid X17","HedonismBot"]
    task_list = ["heavy lifting","materials transport","earth moving","concrete pouring","brick laying"]
    task_sum  = [ 0 for i in range(len(task_list))]
    task_load = [ 0 for i in range(len(task_list))]
    for i in range(len(robo_name)):
        print robo_name[i]
        print "rent hour = %4.3f" % sol['x'][i]
        for j in range(len(task_list)):
            if sol['x'] >= 0:
                task_load[j] = -sol['x'][i]*G[4+j,i]
                print "%20s %4.3f" %(task_list[j],task_load[j])
                task_sum[j] = task_sum[j] + task_load[j]
            else:
                print "N/A"
        print
    
    print "Sum of each tasks"
    for j in range(len(task_list)):
        print "%20s %4.3f" % (task_list[j],task_sum[j])
    sum = 0
    for i in range(4):
        if(sol['x'][i]>0):
            sum += sol['x'][i]*c[i]
    print "Total rent = $ %.2f" % sum

if __name__ == "__main__":
    main()