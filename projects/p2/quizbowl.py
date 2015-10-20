import sklearn.metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier
from numpy import *
import datasets

if not datasets.Quizbowl.loaded:
    datasets.loadQuizbowl()

print '\n\nRUNNING ON EASY DATA\n'
    
print 'training oaa'
X = datasets.QuizbowlSmall.X
Y = datasets.QuizbowlSmall.Y
oaa = OneVsOneClassifier(LinearSVC(random_state=0)).fit(X, Y)
print 'predicting oaa'
oaaDevPred = oaa.predict(datasets.QuizbowlSmall.Xde)
print 'error = %g' % mean(oaaDevPred != datasets.QuizbowlSmall.Yde)

print 'training ava'
ava = OneVsRestClassifier(LinearSVC(random_state=0)).fit(X, Y)
print 'predicting ava'
avaDevPred = ava.predict(datasets.QuizbowlSmall.Xde)
print 'error = %g' % mean(avaDevPred != datasets.QuizbowlSmall.Yde)

print '\n\nRUNNING ON HARD DATA\n'
    
print 'training oaa'
X = datasets.QuizbowlHardSmall.X
Y = datasets.QuizbowlHardSmall.Y
oaa = OneVsOneClassifier(LinearSVC(random_state=0)).fit(X, Y)
print 'predicting oaa'
oaaDevPred = oaa.predict(datasets.QuizbowlHardSmall.Xde)
print 'error = %g' % mean(oaaDevPred != datasets.QuizbowlHardSmall.Yde)

print 'training ava'
ava = OneVsRestClassifier(LinearSVC(random_state=0)).fit(X, Y)
print 'predicting ava'
avaDevPred = ava.predict(datasets.QuizbowlHardSmall.Xde)
print 'error = %g' % mean(avaDevPred != datasets.QuizbowlHardSmall.Yde)

print >>open('predictions.txt', 'w'), avaDevPred

