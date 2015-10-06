# Lab 4: Multiclass

In this lab we'll explore two methods for multiclass to binary
reduction: OAA (one against all) and AllPairs (aka all versus all). I
have (nicely) provided an implementation of OAA for you and a nearly
complete implementation of AllPairs in multiclass.py.

The classification task we'll work with is wine classification (sorry
if you're not a wine snob and this doesn't mean much to you). I
downloaded 4000 wines from allwines.com. Your job is, given the
description of the wine, predict the type of wine. There are two
tasks: WineData has 20 different wines, WineDataSmall is just the
first five of those (sorted roughly by frequency).

You can find the names of the wines both in WineData.labels as well as
the file wines.names.

To start out, be sure to import everything:

```python
>>> from sklearn.tree import DecisionTreeClassifier
>>> import multiclass
>>> import util
>>> from datasets import *
```

To get you started, here's how we can train decision "stumps" (aka
depth=1 decision trees) on the large data set:

```python
>>> h = multiclass.OAA(20, lambda: DecisionTreeClassifier(max_depth=1))
>>> h.train(WineData.X, WineData.Y)
>>> P = h.predictAll(WineData.Xte)
>>> mean(P == WineData.Yte)
0.29499072356215211
```

That means 29% accuracy on this task. The most frequent class is:

```python
>>> mode(WineData.Y)
1
>>> WineData.labels[1]
'Cabernet-Sauvignon'
```

And if you were to always predict label 1, you would get the following
accuracy:

```python
>>> mean(WineData.Yte == 1)
0.17254174397031541
```

So we're doing a bit (12%) better than that using decision stumps.

The default implementation of OAA uses decision tree confidence
(probability of prediction) to weigh the votes. You can switch to
zero/one predictions to see the effect:

```python
>>> P = h.predictAll(WineData.Xte, useZeroOne=True)
>>> mean(P == WineData.Yte)
0.19109461966604824
```

As you can see, this is **markedly worse**.

Switching to the smaller data set for a minute, we can train, say,
depth 3 decision trees:

```python
>>> h = multiclass.OAA(5, lambda: DecisionTreeClassifier(max_depth=3))
>>> h.train(WineDataSmall.X, WineDataSmall.Y)
>>> P = h.predictAll(WineDataSmall.Xte)
>>> mean(P == WineDataSmall.Yte)
0.60393873085339167
>>> mean(WineDataSmall.Yte == 1)
0.40700218818380746
```

So using depth 3 trees we get an accuracy of about 60% (this number
varies a bit), versus a baseline of 41%. That's not too terrible, but
not great.

We can look at what this classifier is doing.

```python
>>> WineDataSmall.labels[0]
'Sauvignon-Blanc'
>>> util.showTree(h.f[0], WineDataSmall.words)
```

This should show the tree that's associated with predicting label 0
(which is stored in h.f[0]). The 1s mean "likely to be
Sauvignon-Blanc" and the 0s mean "likely not to be".

(A) What words are most indicative of *being* Sauvignon-Blanc? Which
words are most indicative of not being Sauvignon-Blanc? What about
Pinot-Noir (label==2)?

(B) Train depth 3 decision trees on the full WineData task (with 20
labels). What accuracy do you get? How long does this take (in
seconds)? One of my least favorite wines is Viognier -- what words are
indicative of this?

(C) Compare the accuracy using zero-one predictions versus using
confidence. How much difference does it make?

# Optional, but part of P2....

Now, go in and complete the AllPairs implementation. You should be able to
train an AllPairs model on the small data set by:

```python
>>> h = AllPairs(5, lambda: DecisionTreeClassifier(max_depth=3)
>>> h.train(WineDataSmall.X, WineDataSmall.Y)
>>> P = h.predictAll(WineDataSmall.Xte)
```

Repeat (A-C) using AllPairs.

