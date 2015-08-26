import sys
import numpy as np
from util import Counter

def loadTextDataBinary(filename, fixedDictionary=None):
    wfreq = Counter()
    h = open(filename, 'r')
    D = []
    for l in h.readlines():
        a = l.split()
        if len(a) > 1:
            y = int(a[0])
            x = {}
            for w in a[1:]:
                x[w] = 1.
            if fixedDictionary is None:
                for w in x.iterkeys():
                    wfreq[w] += 1
            D.append( (x,y) )
    h.close()

    if fixedDictionary is None:
        wid = {}
        widr = []
        maxId = 1
        for w,c in wfreq.iteritems():
            if c >= 20 and c < 0.7*len(D):
                wid[w] = maxId
                widr.append(w)
                maxId += 1
    else:
        wid = { w: n+1 for n,w in enumerate(fixedDictionary) }
        widr = fixedDictionary
        maxId = len(fixedDictionary) + 1
                
    N = len(D)

    Xall = np.zeros((N,maxId-1), dtype=float)
    Yall = np.zeros((N,), dtype=float)
    for n in range(len(D)):
        (x,y) = D[n]
        Yall[n] = y
        for w in x.iterkeys():
            if wid.has_key(w):
                Xall[n,wid[w]-1] = 1.

    return Xall,Yall,widr

def showTree(dt, dictionary):
    left   = dt.tree_.children_left
    right  = dt.tree_.children_right
    thresh = dt.tree_.threshold
    feats  = [ dictionary[i] for i in dt.tree_.feature ]
    value  = dt.tree_.value
    def showTree_(node, s, depth):
        for i in range(depth-1):
            sys.stdout.write('|    ')
        if depth > 0:
            sys.stdout.write('-')
            sys.stdout.write(s)
            sys.stdout.write('-> ')
        if thresh[node] == -2: # leaf
            print 'class %d\t(%d for class 0, %d for class 1)' % (np.argmax(value[node]), value[node][0,0], value[node][0,1])
        else: # internal node
            print '%s?' % feats[node]
            showTree_(left[ node], 'N', depth+1)
            showTree_(right[node], 'Y', depth+1)

    showTree_(0, '', 0)

    
