from numpy import *
from binary import *
import util

class NB(BinaryClassifier):
    """
    This class defines the decision tree implementation.  It comes
    with a partial implementation for the tree data structure that
    will enable us to print the tree in a canonical form.
    """

    def __init__(self, opts):
        self.opts = opts

    def online(self):
        """
        Our decision trees are batch
        """
        return False

    def __repr__(self):
        """
        Return a string representation of the tree
        """
        return str((self.posWeights, self.negWeights))

    def predict(self, X):
        logProbPos = 0.
        logProbNeg = 0.
        for d in range(X.shape[0]):
            logProbPos += X[d] * log( self.posWeights[d] )
            logProbNeg += X[d] * log( self.negWeights[d] )
        return logProbPos - logProbNeg

    def train(self, X, Y):
        N,D  = X.shape

        posX = X[Y>0,:]
        negX = X[Y<0,:]

        self.posWeights = zeros((D,1), dtype=float)
        self.negWeights = zeros((D,1), dtype=float)
        for d in range(D):
            self.posWeights[d] = sum(posX[:,d]) / posX.shape[0]
            self.negWeights[d] = sum(negX[:,d]) / negX.shape[0]


    def getRepresentation(self):
        """
        Return our internal representation: for DTs, this is just our
        tree structure -- i.e., ourselves
        """
        
        return self

