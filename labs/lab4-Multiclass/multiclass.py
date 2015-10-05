from numpy import *

class OAA:
    def __init__(self, K, mkClassifier):
        self.f = []
        self.K = K
        for k in range(K):
            self.f.append(mkClassifier())

    def train(self, X, Y):
        for k in range(self.K):
            print 'training classifier for', k, 'versus rest'
            Yk = 2 * (Y == k) - 1   # +1 if it's k, -1 if it's not k
            self.f[k].fit(X, Yk)

    def predict(self, X, useZeroOne=False):
        vote = zeros((self.K,))
        for k in range(self.K):
            probs = self.f[k].predict_proba(X)
            if useZeroOne:
                vote[k] += 1 if probs[0,1] > 0.5 else 0
            else:
                vote[k] += probs[0,1]   # weighted vote
        return argmax(vote)

    def predictAll(self, X, useZeroOne=False):
        N,D = X.shape
        Y   = zeros(N, dtype=int)
        for n in range(N):
            Y[n] = self.predict(X[n,:], useZeroOne)
        return Y
        

class AllPairs:
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
                # make i,j mean "class i, not class j"
                Xij = None # TODO
                Yij = None # TODO
                self.f[i][j].train(Xij, Yij)

    def predict(self, X, useZeroOne=False):
        vote = zeros((self.K,))
        for i in range(self.K):
            for j in range(i):
                # TODO: figure out how much to vote; also be sure to useZeroOne
                vote[j] += p
                vote[i] -= p
        return argmax(vote)

    def predictAll(self, X, useZeroOne=False):
        N,D = X.shape
        Y   = zeros((N,), dtype=int)
        for n in range(N):
            Y[n] = self.predict(X[n,:], useZeroOne)
        return Y
        
    
