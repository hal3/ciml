from numpy import *
import numpy as np
from util import *
from pylab import *

def kmeans(X, mu0, doPlot=True):
    '''
    X is an N*D matrix of N data points in D dimensions.

    mu is a K*D matrix of initial cluster centers, K is
    the desired number of clusters.

    this function should return a tuple (mu, z, obj) where mu is the
    final cluster centers, z is the assignment of data points to
    clusters, and obj[i] is the kmeans objective function:
      (1/N) sum_n || x_n - mu_{z_n} ||^2
    at iteration [i].

    mu[k,:] is the mean of cluster k
    z[n] is the assignment (number in 0...K-1) of data point n

    you should run at *most* 100 iterations, but may run fewer
    if the algorithm has converged
    '''

    mu = mu0.copy()    # for safety

    N,D = X.shape
    K   = mu.shape[0]

    # initialize assignments and objective list
    z   = zeros((N,), dtype=int)
    obj = []

    # run at most 100 iterations
    for it in range(100):
        # store the old value of z so we can check convergence
        z_old = z.copy()
        
        # recompute the assignment of points to centers
        for n in range(N):
            bestK    = -1
            bestDist = 0
            for k in range(K):
                d = linalg.norm(X[n,:] - mu[k,:])
                if d < bestDist or bestK == -1:
                    bestK = k
                    bestDist = d
            z[n] = bestK

        # recompute means
        for k in range(K):
            mu[k,:] = mean(X[z==k, :], axis=0)

        # compute the objective
        currentObjective = 0
        for n in range(N):
            currentObjective = currentObjective + linalg.norm(X[n,:] - mu[z[n],:]) ** 2 / float(N)
        obj.append(currentObjective)

        print 'Iteration %d, objective=%g' % (it, currentObjective)
        if doPlot:
            plotDatasetClusters(X, mu, z)
            show(block=False)
            x = raw_input("Press enter to continue...")
            if x == "q":
                doPlot = False

        # check to see if we've converged
        if all(z == z_old):
            break

    if doPlot and D==2:
        plotDatasetClusters(X, mu, z)
        show(block=False)

    # return the required values
    return (mu, z, array(obj))

def initialize_clusters(X, K, method):
    '''
    X is N*D matrix of data
    K is desired number of clusters (>=1)
    method is one of:
      determ: initialize deterministically (for comparitive reasons)
      random: just initialize randomly
      ffh   : use furthest-first heuristic

    returns a matrix K*D of initial means.

    you may assume K <= N
    '''

    N,D = X.shape
    mu = zeros((K,D))

    if method == 'determ':
        # just use the first K points as centers
        mu = X[0:K,:].copy()     # be sure to copy otherwise bad things happen!!!

    elif method == 'random':
        # pick K random centers
        dataPoints = range(N)
        permute(dataPoints)
        mu = X[dataPoints[0:K], :].copy()   # ditto above

    elif method == 'ffh':
        # pick the first center randomly and each subsequent
        # subsequent center according to the furthest first
        # heuristic

        # pick the first center totally randomly
        mu[0,:] = X[int(rand() * N), :].copy()    # be sure to copy!

        # pick each subsequent center by ldh
        for k in range(1, K):
            # find m such that data point n is the best next mean, set
            # this to mu[k,:]
            
            ### TODO: YOUR CODE HERE
            util.raiseNotDefined()

    elif method == 'km++':
        # pick the first center randomly and each subsequent
        # subsequent center according to the kmeans++ method
        # HINT: see numpy.random.multinomial
        
        ### TODO: YOUR CODE HERE
        util.raiseNotDefined()

    else:
        print "Initialization method not implemented"
        sys.exit(1)

    return mu


