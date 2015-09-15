import sys,os
from math import *

def loadDigitData(filename, maxExamples=100000):
    h = open(filename, 'r')
    D = []
    for l in h.readlines():
        a = l.split()
        if len(a) > 1:
            y = float(a[0])
            if y > 0.5: y = 1.
            else: y = -1.
            x = {}
            for i in range(1, len(a)):
                v = float(a[i]) / 255.
                if v > 0.:
                    x[i] = v
            D.append( (x,y) )
            if len(D) >= maxExamples:
                break
    h.close()
    return D

def exampleDistance(x1, x2):
    dist = 0.
    for i,v1 in x1.iteritems():
        v2 = 0.
        if x2.has_key(i): v2 = x2[i]
        dist += (v1 - v2) * (v1 - v2)
    for i,v2 in x2.iteritems():
        if not x1.has_key(i):
            dist += v2 * v2
    return sqrt(dist)

# returns list of K (dist, n) where n is the nth training example
def findKNN(D, xhat, K):  # D is the training data, xhat is the test point
    allDist = []
    for n in range(len(D)):
        (x,y) = D[n]
        allDist.append( (exampleDistance(x, xhat), n) )
    allDist.sort()
    return allDist[0:K]

def classifyKNN(D, knn):
    yhat = 0
    for (dist,n) in knn:
        (x,y) = D[n]
        yhat = yhat + y
    if yhat > 0.:
        return 1.
    else:
        return -1.

def computeErrorRate(trainingData, testData, allK):
    maxK = allK[0]
    err = []
    for k in allK:
        if k > maxK: maxK = k;
        err.append(0.)
    for (x,y) in testData:
        knn = findKNN(trainingData, x, maxK)
        for i in range(len(allK)):
            yhat = classifyKNN(trainingData, knn[0:allK[i]])
            if y * yhat < 0:
                err[i] += 1.
    for i in range(len(allK)):
        err[i] /= float(len(testData))
    return err


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print 'usage: python KNN.py [training filename] [testing filename] [K1] [K2] ... [Klast]'
        exit(-1)

    tr = loadDigitData(sys.argv[1])
    te = loadDigitData(sys.argv[2], 100)
    allK = [int(arg) for arg in sys.argv[3:]]
    print "\t".join([str(err) for err in computeErrorRate(tr, te, allK)])
    
    
    
