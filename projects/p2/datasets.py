from numpy import *
from util import *
import csv
import sys
import re

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
    
    
def loadTextDataMC(filename, illegalWords={}):
    wfreq = Counter()
    h = open(filename, 'r')
    D = []
    for l in h.readlines():
        a = l.split()
        if len(a) > 1:
            y = int(a[0])
            x = {}
            for w in a[1:]:
                if not illegalWords.has_key(w):
                    x[w] = 1.
            for w in x.iterkeys():
                wfreq[w] += 1
            D.append( (x,y) )
    h.close()

    wid = {}
    widr = []
    maxId = 1
    for w,c in wfreq.iteritems():
        if c >= 20 and c < 0.7*len(D):
            wid[w] = maxId
            widr.append(w)
            maxId += 1

    N = len(D)

    Xall = zeros((N,maxId-1), dtype=float)
    Yall = zeros((N,), dtype=int)
    for n in range(len(D)):
        (x,y) = D[n]
        Yall[n] = y
        for w in x.iterkeys():
            if wid.has_key(w):
                Xall[n,wid[w]-1] = 1.

    return Xall,Yall,widr


class WineData:
    labels = ['Sauvignon-Blanc', 'Cabernet-Sauvignon', 'Pinot-Noir', 'Pinot-Gris', 'Pinot-Grigio', 'Chardonnay', 'Brut', 'Merlot', 'Shiraz', 'Malbec', 'Zinfandel', 'Cuvee', 'Riesling', 'Chianti', 'Syrah', 'Blend', 'Rhone', 'Viognier', 'Carmenere', 'Moscato']
    
    illegalWords = {'sauvignon': 1, 'blanc': 1, 'cabernet': 1, 'sauvignon': 1, 'pinot': 1, 'noir': 1, 'pinot': 1, 'gris': 1, 'pinot': 1, 'grigio': 1, 'chardonnay': 1, 'brut': 1, 'merlot': 1, 'shiraz': 1, 'malbec': 1, 'zinfandel': 1, 'cuvee': 1, 'riesling': 1, 'chianti': 1, 'syrah': 1, 'blend': 1, 'rhone': 1, 'viognier': 1, 'carmenere': 1, 'moscato': 1}
    
    Xall,Yall,words = loadTextDataMC('data/wines.alldata', illegalWords)
    N,D = Xall.shape
    N0 = int(float(N) * 0.5)
    X = Xall[0:N0,:]
    Y = Yall[0:N0]
    Xte = Xall[N0:,:]
    Yte = Yall[N0:]

class WineDataSmall:
    labels = WineData.labels[0:5]
    X      = WineData.X[WineData.Y < 5, :]
    Y      = WineData.Y[WineData.Y < 5]
    Xte    = WineData.Xte[WineData.Yte < 5, :]
    Yte    = WineData.Yte[WineData.Yte < 5]
    words  = WineData.words

class WineDataBinary:
    labels = WineData.labels[0:2]
    X      = WineData.X[WineData.Y < 2, :]
    Y      = 2 * (WineData.Y[WineData.Y < 2] == 0) - 1
    Xte    = WineData.Xte[WineData.Yte < 2, :]
    Yte    = 2 * (WineData.Yte[WineData.Yte < 2] == 0) - 1
    words  = WineData.words
    

def tokenize(s): return re.sub('([^A-Za-z0-9 ]+)', ' \\1 ', s).split()  # add space around anything not alphanum

def readQuizBowlData(filename, numbersentences):
    train,dev,test = [],[],[]
    data = csv.reader( open(filename, 'r').readlines() )
    header = data.next()
    if header != ['Question ID', 'Fold', 'Category', 'Answer', 'Text']:
        raise Exception('data improperly formatted')
    for item in iter(data):
        y = item[3]
        sentences = item[4].split(' ||| ')
        sentences = sentences[:numbersentences]
        x = tokenize(' '.join(sentences))
        if   item[1] == 'train': train.append( (x,y) )
        elif item[1] == 'dev'  :   dev.append( (x,y) )
        elif item[1] == 'test' :  test.append( (x,y) )
    return train,dev,test

def makeLabelIDs(train, minfreq):
    if minfreq is None or minfreq <= 1:
        labelIds = { label: k+1 for k,label in enumerate(set([y for x,y in train])) }
    else:
        labelIds = {}
        labelCount = {}
        for x,y in train:
            labelCount[y] = labelCount.get(y,0) + 1
        for y,count in labelCount.iteritems():
            if count >= minfreq:
                labelIds[y] = len(labelIds)+1
    return labelIds

def wordToNumpy(word2feature, labelIds, dataset):
    N = 0
    for x,y in dataset:
        if labelIds.has_key(y):
            N += 1
    D = len(word2feature)
    X = zeros((N,D), dtype=float)
    Y = zeros((N,), dtype=int)
    n = 0
    for x,y in dataset:
        if labelIds.has_key(y):
            Y[n] = labelIds[y]
            for word in x:
                if word2feature.has_key(word):
                    X[n, word2feature[word]] += 1.
            n += 1
    return X,Y

class Quizbowl:
    loaded = False
    pass

class QuizbowlSmall:
    loaded = False
    pass

class QuizbowlHard:
    loaded = False
    pass

class QuizbowlHardSmall:
    loaded = False
    pass

def loadQuizbowl0(minlabelfreq, numbersentences, QB):
    train,dev,test = readQuizBowlData('data/questions.csv', numbersentences)
    labelIds = makeLabelIDs(train + dev + test, minlabelfreq)
    print 'total labels: %d' % len(labelIds)

    wordDF = {}
    for x,y in train:
        for word in set(x):
            wordDF[word] = wordDF.get(word,0) + 1
    dictionary = []
    for word,count in wordDF.iteritems():
        if 10 <= count and count <= 5000:
            dictionary.append(word)
    word2feature = { word:d for d,word in enumerate(dictionary) }
    print >>sys.stderr, 'unique features: %d' % len(dictionary)

    QB.X  ,QB.Y   = wordToNumpy(word2feature, labelIds, train)
    QB.Xde,QB.Yde = wordToNumpy(word2feature, labelIds, dev)
    QB.Xte,QB.Yte = wordToNumpy(word2feature, labelIds, test)
    QB.word2feature = word2feature
    QB.dictionary = dictionary
    QB.K = len(labelIds)
    QB.labels = labelIds
    QB.loaded = True

def loadQuizbowl():
    loadQuizbowl0(None, 100, Quizbowl)
    loadQuizbowl0(20  , 100, QuizbowlSmall)
    loadQuizbowl0(None,   2, QuizbowlHard)
    loadQuizbowl0(20  ,   2, QuizbowlHardSmall)
    
