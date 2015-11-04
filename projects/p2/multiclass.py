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
                Xij =  X[ Y==i | Y==j, : ]
                Yij = (Y[ Y==i | Y==j ] == j) * 2 - 1 # +1 if it's j, -1 if it's i
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
        
    
class TreeNode:
    def __init__(self):
        self.isLeaf = True
        self.label  = 0
        self.info   = None

    def setLeafLabel(self, label):
        self.isLeaf = True
        self.label  = label

    def setChildren(self, left, right):
        self.isLeaf = False
        self.left   = left
        self.right  = right

    def isLeaf(self): return self.isLeaf
    
    def getLabel(self):
        if self.isLeaf: return self.label
        else: raise Exception("called getLabel on an internal node!")
        
    def getLeft(self):
        if self.isLeaf: raise Exception("called getLeft on a leaf!")
        else: return self.left
        
    def getRight(self):
        if self.isLeaf: raise Exception("called getRight on a leaf!")
        else: return self.right

    def setNodeInfo(self, info):
        self.info = info

    def getNodeInfo(self): return self.info

    def iterAllLabels(self):
        if self.isLeaf:
            yield self.label
        else:
            for l in self.left.iterAllLabels():
                yield l
            for l in self.right.iterAllLabels():
                yield l

    def iterNodes(self):
        yield self
        if not self.isLeaf:
            for n in self.left.iterNodes():
                yield n
            for n in self.right.iterNodes():
                yield n

    def __repr__(self):
        if self.isLeaf:
            return str(self.label)
        l = repr(self.left)
        r = repr(self.right)
        return '[' + l + ' ' + r + ']'
            

def makeBalancedTree(allK):
    if len(allK) == 0:
        raise Exception("makeBalancedTree: cannot make a tree of 0 classes")

    tree = TreeNode()
    
    if len(allK) == 1:
        tree.setLeafLabel(allK[0])
    else:
        split  = len(allK)/2
        leftK  = allK[0:split]
        rightK = allK[split:]
        leftT  = makeBalancedTree(leftK)
        rightT = makeBalancedTree(rightK)
        tree.setChildren(leftT, rightT)

    return tree

class MCTree:
    def __init__(self, tree, mkClassifier):
        self.f = []
        self.tree = tree
        for n in self.tree.iterNodes():
            n.setNodeInfo(   mkClassifier()  )

    def train(self, X, Y):
        for n in self.tree.iterNodes():
            if n.isLeaf:   # don't need to do any training on leaves!
                continue

            # otherwise we're an internal node
            leftLabels  = list(n.getLeft().iterAllLabels())
            rightLabels = list(n.getRight().iterAllLabels())

            print 'training classifier for', leftLabels, 'versus', rightLabels

            # compute the training data, store in thisX, thisY
            ### TODO: YOUR CODE HERE
            util.raiseNotDefined()

            n.getNodeInfo().train(thisX, thisY)

    def predict(self, X):
        ### TODO: YOUR CODE HERE
        util.raiseNotDefined()

    def predictAll(self, X):
        N,D = X.shape
        Y   = zeros((N,), dtype=int)
        for n in range(N):
            Y[n] = self.predict(X[n,:])
        return Y
        
def getMyTreeForWine():
    return makeBalancedTree(20)

