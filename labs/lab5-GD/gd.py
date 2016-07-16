from pylab import *
from numpy import *
import time

delta = 0.02

def func1(x):
    return (x[0] ** 2 + x[1] ** 2,
            array([2*x[0], 2*x[1]]),
            array([0,0]))

def func2(x):
    return (x[0] ** 2 + 2 * x[1] ** 2 + x[0] * x[1],
            array([2*x[0] + x[1], 4*x[1] + x[0]]),
            array([0,0]))

def func3(x):
    return (x[0] ** 2 + 10 * x[1] ** 2,
            array([2*x[0], 20*x[1]]),
            array([0,0]))

def computeF(x,y,X,f):
    F = 0 * X
    for i in xrange(x.shape[0]):
        for j in xrange(y.shape[0]):
            F[i,j],_,_ = f(array([x[i],y[j]]))
    return F

def gradStep(f,x,eta,noiseRate):
    _,grad,_ = f(x)
    grad += noiseRate * randn(grad.shape[0])
    size=norm(grad)/50
    arrow(x[0],x[1],-eta*grad[0],-eta*grad[1],fc='b',ec='b',head_length=size,head_width=size)
    show(False)
    x1 = x - eta * grad
    return x1
                            

def sleepIt(sleepTime):
    if sleepTime is None:
        raw_input('Press enter to continue...')
    else:
        time.sleep(sleepTime)
    
def runGD(f,x0,eta,noiseRate=0.0,multiplot=False,sleepTime=None,drawAverageW=False):  # sleepTime=None means wait for enter
    x = arange(-2.0, 2.0, delta)
    y = arange(-2.0, 2.0, delta)
    X,Y = meshgrid(x,y)
    F = computeF(x,y,X,f).T

    x_avg = x0.copy()
    
    _,_,xopt = f(x0)
    
    figure()
    if multiplot:
        subplot(132)
        title('function value')
        subplot(133)
        title('||x - opt||')
        subplot(131)
    contour(X,Y,F,20)
    show(False)
    draw()

    epoch = []
    fval  = []
    dopt  = []

    i = 0
    while True:
        if multiplot: subplot(131)
        plot(x0[0],x0[1],'bo')
        epoch.append(i)
        fval.append(f(x0)[0])
        dopt.append(norm(x0-xopt))
        i += 1
        if drawAverageW: plot(x_avg[0]/i,x_avg[1]/i,'kx')
        if multiplot:
            subplot(132)
            plot(array(epoch),array(fval), 'k-')
            subplot(133)
            plot(array(epoch),array(dopt), 'k-')
            
        draw()
        sleepIt(sleepTime if i > 1 else None)
        if multiplot: subplot(131)
        eta_i = eta if isinstance(eta, float) or isinstance(eta, int) else eta(i)
        x0 = gradStep(f,x0,eta_i,noiseRate)
        x_avg += x0
        draw()
        sleepIt(sleepTime)
        print x0

# runGD(func1, array([-1.5,1.2]), 0.1)
# runGD(func1, array([-1.5,1.2]), 0.9)

# runGD(func2, array([1.5,1.5]), 0.1)
# runGD(func2, array([1.5,-1.5]), 0.9)
