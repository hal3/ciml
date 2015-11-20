import sys
import inspect
import random
from numpy import *
from pylab import *

def raiseNotDefined():
  print "Method not implemented: %s" % inspect.stack()[1][3]    
  sys.exit(1)

def permute(a):
  """
  Randomly permute the elements in array a
  """
  for n in range(len(a)):
    m = int(rand() * (len(a) - n)) + n
    t = a[m]
    a[m] = a[n]
    a[n] = t
    
def splitTrainTest(X0, Y0, freqTest):
  """
  Split data in X0/Y0 into train/test data with freqTest
  frequency of test points
  """
  N,D = X0.shape
  isTest = zeros(N, dtype=bool)
  for n in range(0, N, freqTest):
    isTest[n] = True
  X   = X0[isTest==False, :]
  Y   = Y0[isTest==False]
  Xte = X0[isTest, :]
  Yte = Y0[isTest]

  return (X,Y,Xte,Yte)


def uniq(seq, idfun=None): 
  # order preserving
  if idfun is None:
    def idfun(x): return x
  seen = {}
  result = []
  for item in seq:
    marker = idfun(item)
    # in old Python versions:
    # if seen.has_key(marker)
    # but in new ones:
    if marker in seen: continue
    seen[marker] = 1
    result.append(item)
  return result

def mode(seq):
  if len(seq) == 0:
    return 1.
  else:
    cnt = {}
    for item in seq:
      if cnt.has_key(item):
        cnt[item] += 1
      else:
        cnt[item] = 1
    maxItem = seq[0]
    for item,c in cnt.iteritems():
      if c > cnt[maxItem]:
        maxItem = item
    return maxItem

def plotDataset(X):
  plot(X[:,0], X[:,1], 'bx')

def plotDatasetClusters(X, mu, z):
  colors = array(['b','r','m','k','g','c','y','b','r','m','k','g','c','y','b','r','m','k','g','c','y','b','r','m','k','g','c','y','b','r','m','k','g','c','y'])
  plot(X[:,0], X[:,1], 'w.')
  hold(True)
  for k in range(mu.shape[0]):
    plot(X[z==k,0], X[z==k,1], colors[k] + '.')
    plot(array([mu[k,0]]), array([mu[k,1]]), colors[k] + 'x')
  hold(False)

def sqrtm(M):
    (U,S,VT) = svd(M)
    D = diag(sqrt(S))
    return dot(dot(U,D),VT)

def normalLikelihood(x, mu, Si):
  D = len(x)
  v = dot((x - mu), dot(inv(Si), (x-mu).T))
  n = ((2 * pi) ** (-D/2)) * (det(Si) ** (-1/2))
  return (n * exp(-0.5 * v))

def plotDatasetEM(X, mu, Si, gamma):
  colors = array(['b','r','m','k','g','c','y','b','r','m','k','g','c','y','b','r','m','k','g','c','y','b','r','m','k','g','c','y','b','r','m','k','g','c','y'])
  fig = figure(num=None)
  plot(X[:,0], X[:,1], 'w.')
  ax  = fig.add_axes([0,0,1,1])
  trans = ax.transAxes
  rads = arange(0, 2*pi + 2*pi/40, 2*pi/40)
  unitc = vstack((sin(rads),cos(rads))).T
  hold(True)
  for k in range(mu.shape[0]):
    plot(array([mu[k,0]]), array([mu[k,1]]), colors[k] + 'x')
    r  = dot(unitc, sqrtm(Si[k,:,:])) + mu[k,:]
    r2 = dot(unitc, 2*sqrtm(Si[k,:,:])) + mu[k,:]
    plot(r[:,0], r[:,1], colors[k] + '-')
    plot(r2[:,0], r2[:,1], colors[k] + ':')
  for n in range(X.shape[0]):
    k = argmax(gamma[n,:])
    plot(array([X[n,0]]), array([X[n,1]]), colors[k] + '.')
    aa = gamma[n,:].copy()
    aa = aa / sum(aa)
    cumul = 0
    for k in range(mu.shape[0]):
      wedge = matplotlib.patches.Wedge(array([X[n,0], X[n,1]]), 0.2, cumul, cumul+aa[k]*360, fc=colors[k])
      wedge.set_alpha(0.25)
      ax.add_patch(wedge)
      cumul = cumul + 360*aa[k]
  hold(False)

def drawDigits(X,Y):
  N,D = X.shape
  order = arange(N)
  permute(order)

  figure()
  for i in range(64):
    if i >= len(order):
      break
    subplot(8, 8, i+1)
    imshow(-X[order[i],:].reshape(28,28).T, cmap=cm.gist_gray)
    text(0,6,str(Y[order[i]]),color='blue')
    axis('off')


def addLog(x,y):
  if x == -inf:
    return y
  elif y == -inf:
    return x
  elif x - y > 32:
    return x
  elif x > y:
    return x + log(1 + exp(y-x))
  elif y - x > 32:
    return y
  else:
    return y + log(1 + exp(x-y))


def normalizeLog(a):
  s = -inf
  for v in a:
    s = addLog(s, v)
  return exp(a - s)




