from numpy import *
from util import *

class TennisData:
    #              Outlook      Temperature  Hum   Wind
    #             S?  O?  R?     H?  M?  C?    H?    S?
    X = array([[  1,  0,  0,     1,  0,  0,    1,    0   ],
               [  1,  0,  0,     1,  0,  0,    1,    1   ],
               [  0,  1,  0,     1,  0,  0,    1,    0   ],
               [  0,  0,  1,     0,  1,  0,    1,    0   ],
               [  0,  0,  1,     0,  0,  1,    0,    0   ],
               [  0,  0,  1,     0,  0,  1,    0,    1   ],
               [  0,  1,  0,     0,  0,  1,    0,    1   ],
               [  1,  0,  0,     0,  1,  0,    1,    0   ],
               [  1,  0,  0,     0,  0,  1,    0,    0   ],
               [  0,  0,  1,     0,  1,  0,    0,    0   ],
               [  1,  0,  0,     0,  1,  0,    0,    1   ],
               [  0,  1,  0,     0,  1,  0,    1,    1   ],
               [  0,  1,  0,     1,  0,  0,    0,    0   ],
               [  0,  0,  1,     0,  1,  0,    1,    1   ]
               ], dtype=float)

    Y = array([ -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1 ], dtype=float)

    #              Outlook      Temperature  Hum   Wind
    #             S?  O?  R?     H?  M?  C?    H?    S?
    Xte=array([[  1,  0,  0,     1,  0,  0,    1,    0   ],
               [  1,  0,  0,     1,  0,  0,    1,    1   ],
               [  0,  0,  1,     0,  0,  1,    0,    0   ],
               [  0,  1,  0,     0,  0,  1,    0,    1   ],
               [  1,  0,  0,     0,  0,  1,    0,    0   ],
               [  0,  0,  1,     0,  1,  0,    1,    1   ]
               ], dtype=float)

    Yte=array([ -1, -1, 1, 1, 1, -1 ], dtype=float)


class TwoDAxisAligned:
    X = array([[ 0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  0.1,
                 0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  0.1,  0.2,
                 0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  0.1,  0.2,  0.3,
                 0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  0.1,  0.2,  0.3,  0.4,
                 0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  0.1,  0.2,  0.3,  0.4,  0.5,
                 0.6,  0.7,  0.8,  0.9,  1. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,
                 0.7,  0.8,  0.9,  1. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,
                 0.8,  0.9,  1. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,
                 0.9,  1. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,
                 1. ],
               [ 0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.2,
                 0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.3,  0.3,
                 0.3,  0.3,  0.3,  0.3,  0.3,  0.3,  0.3,  0.3,  0.4,  0.4,  0.4,
                 0.4,  0.4,  0.4,  0.4,  0.4,  0.4,  0.4,  0.5,  0.5,  0.5,  0.5,
                 0.5,  0.5,  0.5,  0.5,  0.5,  0.5,  0.6,  0.6,  0.6,  0.6,  0.6,
                 0.6,  0.6,  0.6,  0.6,  0.6,  0.7,  0.7,  0.7,  0.7,  0.7,  0.7,
                 0.7,  0.7,  0.7,  0.7,  0.8,  0.8,  0.8,  0.8,  0.8,  0.8,  0.8,
                 0.8,  0.8,  0.8,  0.9,  0.9,  0.9,  0.9,  0.9,  0.9,  0.9,  0.9,
                 0.9,  0.9,  1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1. ,
                 1. ]]).T - 0.45
    Y = (X[:,0] > 0.1) * 2 - 1.

    Xte = X - 0.05
    Yte = (Xte[:,0] > 0.1) * 2 - 1.

    
class TwoDDiagonal:
    X = array([[ 0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  0.1,
                 0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  0.1,  0.2,
                 0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  0.1,  0.2,  0.3,
                 0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  0.1,  0.2,  0.3,  0.4,
                 0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  0.1,  0.2,  0.3,  0.4,  0.5,
                 0.6,  0.7,  0.8,  0.9,  1. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,
                 0.7,  0.8,  0.9,  1. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,
                 0.8,  0.9,  1. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,
                 0.9,  1. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,
                 1. ],
               [ 0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.2,
                 0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.2,  0.3,  0.3,
                 0.3,  0.3,  0.3,  0.3,  0.3,  0.3,  0.3,  0.3,  0.4,  0.4,  0.4,
                 0.4,  0.4,  0.4,  0.4,  0.4,  0.4,  0.4,  0.5,  0.5,  0.5,  0.5,
                 0.5,  0.5,  0.5,  0.5,  0.5,  0.5,  0.6,  0.6,  0.6,  0.6,  0.6,
                 0.6,  0.6,  0.6,  0.6,  0.6,  0.7,  0.7,  0.7,  0.7,  0.7,  0.7,
                 0.7,  0.7,  0.7,  0.7,  0.8,  0.8,  0.8,  0.8,  0.8,  0.8,  0.8,
                 0.8,  0.8,  0.8,  0.9,  0.9,  0.9,  0.9,  0.9,  0.9,  0.9,  0.9,
                 0.9,  0.9,  1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1. ,
                 1. ]]).T - 0.45
    Y = (X[:,0] + 3 * X[:,1] > 0) * 2 - 1.

    Xte = X - 0.05
    Yte = (Xte[:,0] + 3 * Xte[:,1] > 0.4) * 2 - 1.
    

def loadTextData(filename):
    wfreq = Counter()
    h = open(filename, 'r')
    D = []
    meta = []
    for l in h.readlines():
        meta_split = l.strip().split('\t')
        a = meta_split[0].split()
        if len(meta_split) > 1:
            meta.append(meta_split[1])
        else:
            meta.append('')
        if len(a) > 1:
            y = float(a[0])
            if y > 0.5: y = 1.
            else: y = -1.
            x = {}
            for w in a[1:]:
                x[w] = x.get(w,0) + 1.
            for w in x.iterkeys():
                wfreq[w] += 1
            D.append( (x,y) )
    h.close()

    wid = {}
    widr = []
    maxId = 1
    for w,c in wfreq.iteritems():
        if c >= 10 and c < 0.7*len(D):
            wid[w] = maxId
            widr.append(w)
            maxId += 1

    N = len(D)

    Xall = zeros((N,maxId-1), dtype=float)
    Yall = zeros((N,), dtype=float)
    for n in range(len(D)):
        (x,y) = D[n]
        Yall[n] = y
        for w in x.iterkeys():
            if wid.has_key(w):
                Xall[n,wid[w]-1] = 1.

    return Xall,Yall,widr,array(meta)

def loadDigitData(filename):
    h = open(filename, 'r')
    X0 = []
    Y0 = []
    for l in h.readlines():
        a = l.split()
        if len(a) > 1:
            y = float(a[0])
            if y > 0.5: Y0.append(1.)
            else: Y0.append(-1.)
            X0.append(array([float(v)/255. for v in a[1:]]))
    h.close()
    return array(X0), array(Y0)

        
class SentimentData:
    Xall,Yall,words,meta = loadTextData('data/sentiment.all')
    N,D = Xall.shape
    N0 = int(float(N) * 0.6)
    N1 = int(float(N) * 0.8)
    X = Xall[0:N0,:]
    Y = Yall[0:N0]
    Xde = Xall[N0:N1,:]
    Yde = Yall[N0:N1]
    Xte = Xall[N1:,:]
    Yte = Yall[N1:]

class DigitData:
    Xall,Yall = loadDigitData('data/1vs2.all')
    N,D = Xall.shape
    N0 = int(float(N) * 0.5)
    X = Xall[0:N0,:]
    Y = Yall[0:N0]
    Xte = Xall[N0:,:]
    Yte = Yall[N0:]

class RecipeData:
    Xall,Yall,words,meta = loadTextData('data/recipes.all')
    N,D = Xall.shape
    N0 = int(float(N) * 0.6)
    N1 = int(float(N) * 0.8)
    X = Xall[0:N0,:]
    Y = Yall[0:N0]
    T = meta[0:N0]
    Xde = Xall[N0:N1,:]
    Yde = Yall[N0:N1]
    Tde = meta[N0:N1]
    Xte = Xall[N1:,:]
    Yte = Yall[N1:]
    Tte = meta[N1:]

    
def savePredictions(filename, Yhat):
    with open(filename, 'w') as h:
        for y in Yhat:
            print >>h, str(y)
    print 'saved!'

