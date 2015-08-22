from binary import *
from util import *
from numpy import *

class OVA:
    def __init__(self, K, mkClassifier):
        self.f = []
        self.K = K
        for k in range(K):
            self.f.append(mkClassifier())

    def train(self, X, Y):
        for k in range(self.K):
            print 'training classifier for', k, 'versus rest'
            Yk = 2 * (Y == k) - 1   # +1 if it's k, -1 if it's not k
            self.f[k].train(X, Yk)

    def predict(self, X):
        vote = zeros((self.K,))
        for k in range(self.K):
            vote[k] += self.f[k].predict(X)
        return argmax(vote)

    def predictAll(self, X):
        N,D = X.shape
        Y   = zeros(N, dtype=int)
        for n in range(N):
            Y[n] = self.predict(X[n,:])
        return Y
        

class AVA:
    def __init__(self, K, mkClassifier):
        self.f = []
        self.K = K
        for i in range(K):
            self.f.append([])
        for j in range(K):
            for i in range(j):
                self.f[j].append(mkClassifier())

    def train(self, X, Y):
        for i in range(self.K):
            for j in range(i):
                print 'training classifier for', i, 'versus', j
                Xij = None # TODO
                Yij = None # TODO: # +1 if it's j, -1 if it's i
                self.f[i][j].train(Xij, Yij)

    def predict(self, X):
        vote = zeros((self.K,))
        for i in range(self.K):
            for j in range(i):
                p = self.f[i][j].predict(X)
                vote[j] += p
                vote[i] -= p
        return argmax(vote)

    def predictAll(self, X):
        N,D = X.shape
        Y   = zeros((N,), dtype=int)
        for n in range(N):
            Y[n] = self.predict(X[n,:])
        return Y
        
    
