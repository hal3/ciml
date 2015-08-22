"""
This defines an abstract class for binary classification.  It supports
both online algorithms (like perceptron) and batch algorithm (like
gradient descent).
"""



import util
from numpy import *

class BinaryClassifier:
    """
    Our abstract class.

    If you implement this class, you must do one of the following:
      (1) be online and implement 'nextExample' and 'nextIteration'
      (2) be batch  and implement 'train'
    """

    def __init__(self, opts):
        self.opts = opts

    def setOption(self, optName, optVal):
        """
        set a particular option
        """
        self.opts[optName] = optVal

    def isOnline(self):
        """
        return True if you are an online algorithm
        """

    def reset(self):
        """
        Reset the state of an online learning to as if it had seen nothing
        """
        
    def predict(self, X):
        """
        X is a vector that we're supposed to make a prediction about.
        Semantically, a return value <0 means class -1 and a return
        value >=0 means class +1
        """
        util.raiseNotDefined()

    def predictAll(self, X):
        """
        X is a matrix that we're supposed to make a bunch of predictions about.
        Semantically, a return value <0 means class -1 and a return
        value >=0 means class +1
        """
        N,D = X.shape
        Y   = zeros(N)
        for n in range(N):
            Y[n] = self.predict(X[n,:])
        return Y

    def nextExample(self, X):
        """
        (ONLINE ONLY)
        
        X is a vector training example and Y is its associated class.
        We're guaranteed that Y is either +1 or -1.
        """
        util.raiseNotDefined()

    def nextIteration(self):
        """
        (ONLINE ONLY)
        
        Indicates to us that we've made a complete pass through the
        training data.
        """
        util.raiseNotDefined()

    def train(self, X, Y):
        """
        (BATCH ONLY)

        X is a matrix of data points, Y is a vector of +1/-1 classes.
        """
        if self.online():
            for epoch in range(self.opts['numEpoch']):
                # loop over every data point
                for n in range(X.shape[0]):
                    # supply the example to the online learner
                    self.nextExample(X[n], Y[n])

                # tell the online learner that we're
                # done with this iteration
                self.nextIteration()
        else:
            util.raiseNotDefined()

    def getRepresentation(self):
        """
        Some algorithm-specific representation
        """
        util.raiseNotDefined()


