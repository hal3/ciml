from math import *
import numpy as np
import matplotlib.pyplot as plt

def divide(a,b):
    if b == 0:
        return 1
    return a/b

def makeOnePreRecCurve(Y, P, doHold=True, color='b-'):
    N = Y.shape[0]
    a = np.array([(P[i], Y[i]) for i in range(N)], dtype=[('p',np.float),('y',np.float)])
    S = 0.0
    T = sum(a['y'])
    I = 0.0
    a = np.sort(a)
    curve = {}
    curve[0.0] = 1.0
    curve[1.0] = 0.0      # we can always get this by declaring nothing
    curve[T/N] = 1.0      # and if we declare everything
    maxF = 0.0
    for n in range(N-1,-1,-1):   # go over it backward
        # we "add" a[n] into the "yes" set
        # which means that S always increases by one
        # I increases by one if a[n][1] is true
        S += 1.0
        if a[n]['y'] > 0.5:
            I += 1.0
        pre = divide(I, S)
        rec = divide(I, T)
        if pre > 0 and rec > 0:
            f = 2 * pre * rec / (pre + rec)
            if f > maxF: maxF = f
        if rec > 0 and (not curve.has_key(pre) or rec > curve[pre]):
            curve[pre] = rec
    curve = curve.items()
    curve = np.array(curve, dtype=[('p',np.float), ('r',np.float)])
    curve = list(np.sort(curve))
    curve.append((1,0))
    curve = np.array(curve, dtype=[('p',np.float), ('r',np.float)])
    N = curve.shape[0]
    maxFutureValue = np.ones((N,), dtype=float)
    maxFutureValue[N-1] = curve[N-1][1]
    for n in range(N-2,-1,-1):
        maxFutureValue[n] = max(maxFutureValue[n+1], curve[n][1])
    keep = curve['r'] >= maxFutureValue
    if doHold: plt.hold(False)
    plt.plot(curve[keep]['p'], curve[keep]['r'], color)
    if doHold: plt.hold(True)
    plt.axis([0,1.05,0,1.05])
    plt.xlabel('Precision')
    plt.ylabel('Recall')
    if doHold: plt.show()
    return maxF

def makeManyCurves(Y, allP):
    colors = ['b-','r-','g-','k-','m-']
    plt.hold(False)
    legList = []
    for i in range(len(allP)):
        f = makeOnePreRecCurve(Y, allP[i], False, colors[i % 5])
        legList.append('Data ' + str(i) + ' (F=' + str(f)[0:5] + ')')
        plt.hold(True)
    plt.legend(legList, loc=3)
    plt.show()
    
def ttest(Y, P0, P1, restrictTo=None):
    # return the t-statistic and p-value for the hypothesis test
    # that P1 is better than P0
    
    if restrictTo is not None:
        Y = Y[0:restrictTo]
        P0 = P0[0:restrictTo]
        P1 = P1[0:restrictTo]
    
    N  = float(Y.shape[0])
    if N <= 0: return 0.,"not significant at 90% level"

    # first, compute the error of P0 and P1
    a  = (Y>0.5) != (P0>0.5)
    b  = (Y>0.5) != (P1>0.5)
    
    # compute the means
    mu_a = np.mean(a)
    mu_b = np.mean(b)

    # center the errors
    ahat = 0   # TODO
    bhat = 0   # TODO

    # compute the denominator
    diff = 0   # TODO

    # make sure it's not infinite
    diff = min(diff, 1e10)

    # compute the t-statistic
    t = 0 # TODO

    # look up significance
    sig = "not significant at 90% level"
    if   t >= 2.58: sig = "significant at 99.5% level"
    elif t >= 1.96: sig = "significant at 97.5% level"
    elif t >= 1.64: sig = "significant at 95% level"
    elif t >= 1.28: sig = "significant at 90% level"

    return t,sig

def loadFile(fname):
    h = open(fname, 'r')
    a = np.array([float(s) for s in h.readlines()])
    h.close()
    return a

Y = loadFile('prediction.truth')
allP = [loadFile('prediction.top' + str(i)) for i in range(1,4)]

    
