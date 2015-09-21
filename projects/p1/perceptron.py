"""
In perceptron.py, you will implement the perceptron algorithm for
binary classification.  You will implement both the vanilla perceptron
updates as well as the averaged perceptron updates.
"""

from numpy import *

from binary import *
import util

class Perceptron(BinaryClassifier):
    """
    This class defines the perceptron implementation of a binary
    classifier.  See binary.py for details on the abstract class that
    this implements.
    """

    def __init__(self, opts):
        """
        Initialize our internal state.  You probably need to (at
        least) keep track of a weight vector and a bias.  We'll just
        call the 'reset' function to do this for us.

        We will also want to compute simple statistics about how the
        training of the perceptron is going.  In particular, you
        should keep track of how many updates have been made total.
        """

        BinaryClassifier.__init__(self, opts)
        self.opts = opts
        self.reset()

    def reset(self):
        """
        Reset the internal state of the classifier.
        """

        self.weights = 0    # our weight vector
        self.bias    = 0    # our bias
        self.numUpd  = 0    # number of updates made

    def online(self):
        """
        Our perceptron is online
        """
        return True

    def __repr__(self):
        """
        Return a string representation of the tree
        """
        return    "w=" + repr(self.weights)   +  ", b=" + repr(self.bias)

    def predict(self, X):
        """
        X is a vector that we're supposed to make a prediction about.
        Our return value should be the margin at this point.
        Semantically, a return value <0 means class -1 and a return
        value >=0 means class +1
        """

        if self.numUpd == 0:
            return 0          # failure
        else:
            return dot(self.weights, X) + self.bias   # this is done for you!

    def nextExample(self, X, Y):
        """
        X is a vector training example and Y is its associated class.
        We're guaranteed that Y is either +1 or -1.  We should update
        our weight vector and bias according to the perceptron rule.
        """

        # check to see if we've made an error
        if Y * self.predict(X) <= 0:   ### SOLUTION-AFTER-IF
            self.numUpd  = self.numUpd  + 1

            # perform an update
            self.weights = util.raiseNotDefined()    ### TODO: YOUR CODE HERE

            self.bias    = util.raiseNotDefined()    ### TODO: YOUR CODE HERE


    def nextIteration(self):
        """
        Indicates to us that we've made a complete pass through the
        training data.  This function doesn't need to do anything for
        the perceptron, but might be necessary for other classifiers.
        """
        return   # don't need to do anything here
        

    def getRepresentation(self):
        """
        Return a tuple of the form (number-of-updates, weights, bias)
        """

        return (self.numUpd, self.weights, self.bias)

