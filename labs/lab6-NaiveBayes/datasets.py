from numpy import *
from util import *


def loadTextData(filename):
    wfreq = Counter()
    h = open(filename, 'r')
    D = []
    for l in h.readlines():
        a = l.split()
        if len(a) > 1:
            y = float(a[0])
            if y > 0.5: y = 1.
            else: y = -1.
            x = {}
            for w in a[1:]:
                x[w] = 1.
            for w in x.iterkeys():
                wfreq[w] += 1
            D.append( (x,y) )
    h.close()

    wid = {}
    widr = []
    maxId = 1
    for w,c in wfreq.iteritems():
        if c >= 100 and c < 0.7*len(D):
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

    return Xall,Yall,widr

class SentimentData:
    Xall,Yall,words = loadTextData('data/sentiment.all')
    N,D = Xall.shape
    N0 = int(float(N) * 0.6)
    N1 = int(float(N) * 0.8)
    X = Xall[0:N0,:]
    Y = Yall[0:N0]
    Xde = Xall[N0:N1,:]
    Yde = Yall[N0:N1]
    Xte = Xall[N1:,:]
    Yte = Yall[N1:]
