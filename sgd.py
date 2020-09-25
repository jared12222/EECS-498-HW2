def sgd(f,fp,x0,i_range,t = 1., iteration = 1000):
    import numpy as np
    x = [x0]
    for n in range(iteration):
        i = np.random.randint(1,i_range)
        dx = -fp(x[-1],i)
        x.append(x[-1] + t*dx)
    return x