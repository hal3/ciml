# Project 1: Classification

The goal of this project is to extend some of the work you've done in
the labs and implement some of the techniques from scratch.




## Introduction

The code for this project consists of several Python files, some of
which you will need to read and understand in order to complete the
assignment, and some of which you can ignore.

### Files You'll Edit

``dumbClassifiers.py``: This contains a handful of "warm up"
classifiers to get you used to our classification framework.
  
``dt.py``: Will be your simple implementation of a decision tree classifier.
  
``knn.py``: This is where your nearest-neighbor classifier modifications
will go.

``perceptron.py``: Take a guess :).

### Files you might want to look at
  
``binary.py``: Our generic interface for binary classifiers (actually
works for regression and other types of classification, too).

``datasets.py``: Where a handful of test data sets are stored.

``util.py``: A handful of useful utility functions: these will
undoubtedly be helpful to you, so take a look!

``runClassifier.py``: A few wrappers for doing useful things with
classifiers, like training them, generating learning curves, etc.

``mlGraphics.py``: A few useful plotting commands

``data/*``: all of the datasets we'll use.

### What to Submit

You will handin all of the python files listed above under "Files
you'll edit" as well as a partners.txt file that lists the **names** and
**last four digits of the UID** of all members in your team.  Finally,
you'll hand in a **writeup.pdf** file that answers all the written
questions in this assignment (denoted by **WU#** in this file).


#### Autograding

Your code will be autograded for technical correctness. Please **do
not** change the names of any provided functions or classes within the
code, or you will wreak havoc on the autograder. However, the
correctness of your implementation -- not the autograder's output --
will be the final judge of your score.  If necessary, we will review
and grade assignments individually to ensure that you receive due
credit for your work.



## Warming up to Classifiers (10%)

Let's begin our foray into classification by looking at some very
simple classifiers.  There are three classifiers
in ``dumbClassifiers.py``, one is implemented for you, the other
two you will need to fill in appropriately.

The already implemented one is ``AlwaysPredictOne``, a classifier
that (as its name suggest) always predicts the positive class.  We're
going to use the ``TennisData`` dataset from ``datasets.py``
as a running example.  So let's start up python and see how well this
classifier does on this data.  You should begin by
importing ``util``, ``datasets``, ``binary``
and ``dumbClassifiers``.  Also, be sure you always have ``from
  numpy import **`` and ``from pylab import **`` activated.

```python
>>> h = dumbClassifiers.AlwaysPredictOne({})
>>> h
AlwaysPredictOne
>>> h.train(datasets.TennisData.X, datasets.TennisData.Y)
>>> h.predictAll(datasets.TennisData.X)
array([ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.])
```

Indeed, it looks like it's always predicting one!

Now, let's compare these predictions to the truth.  Here's a very
clever way to compute accuracies (**WU1:** why is this computation
equivalent to computing classification accuracy?):

```
>>> mean((datasets.TennisData.Y > 0) == (h.predictAll(datasets.TennisData.X) > 0))
0.6428571428571429
```

That's training accuracy; let's check test accuracy:

```
>>> mean((datasets.TennisData.Yte > 0) == (h.predictAll(datasets.TennisData.Xte) > 0))
0.5
```

Okay, so it does pretty badly.  That's not surprising, it's really not
learning anything!!!

Now, let's use some of the built-in functionality to help do some of
the grunt work for us.  You'll need to import ``runClassifier``.

```
>>> runClassifier.trainTestSet(h, datasets.TennisData)
Training accuracy 0.642857, test accuracy 0.5
```

Very convenient!

Now, your first implementation task will be to implement the missing
functionality in ``AlwaysPredictMostFrequent``.  This actually
will "learn" something simple.  Upon receiving training data, it will
simply remember whether +1 is more common or -1 is more common.  It
will then always predict this label for future data.  Once you've
implemented this, you can test it:

```
>>> h = dumbClassifiers.AlwaysPredictMostFrequent({})
>>> runClassifier.trainTestSet(h, datasets.TennisData)
Training accuracy 0.642857, test accuracy 0.5
>>> h
AlwaysPredictMostFrequent(1)
```

Okay, so it does the same as ``AlwaysPredictOne``, but that's
because +1 is more common in that training data.  We can see a
difference if we change to a different dataset: ``GenderData`` is
the data you've seen before, now Python-ified.

```
>>> runClassifier.trainTestSet(dumbClassifiers.AlwaysPredictOne({}), datasets.GenderData)
Training accuracy 0.503168, test accuracy 0.489
>>> runClassifier.trainTestSet(dumbClassifiers.AlwaysPredictMostFrequent({}), datasets.GenderData)
Training accuracy 0.503168, test accuracy 0.489
```

Since the majority class is "1", these do the same here.

The last dumb classifier we'll implement
is ``FirstFeatureClassifier``.  This actually does something
slightly non-trivial.  It looks at the first feature
(i.e., ``X[0]``) and uses this to make a prediction.  Based on
the training data, it figures out what is the most common class for
the case when ``X[0] > 0`` and the most common class for the case
when ``X[0] <= 0``.  Upon receiving a test point, it checks the
value of ``X[0]`` and returns the corresponding class.  Once
you've implemented this, you can check it's performance:

```
>>> runClassifier.trainTestSet(dumbClassifiers.FirstFeatureClassifier({}), datasets.TennisData)
Training accuracy 0.714286, test accuracy 0.666667
>>> runClassifier.trainTestSet(dumbClassifiers.FirstFeatureClassifier({}), datasets.GenderData)
Training accuracy 0.504668, test accuracy 0.4905
>>> runClassifier.trainTestSet(dumbClassifiers.FirstFeatureClassifier({}), datasets.SentimentData)
Training accuracy 0.540833, test accuracy 0.5025
```


## Decision Trees (30%)

Our next task is to implement a decision tree classifier.  There is
stub code in ``dt.py`` that you should edit.  Decision trees are
stored as simple data structures.  Each node in the tree has
a ``.isLeaf`` boolean that tells us if this node is a leaf (as
opposed to an internal node).  Leaf nodes have a ``.label`` field
that says what class to return at this leaf.  Internal nodes have:
a ``.feature`` value that tells us what feature to split on;
a ``.left`` *tree* that tells us what to do when the feature
value is *less than 0.5*; and a ``.right`` *tree* that
tells us what to do when the feature value is *at least 0.5*.
To get a sense of how the data structure works, look at
the ``displayTree`` function that prints out a tree.

Your first task is to implement the training procedure for decision
trees.  We've provided a fair amount of the code, which should help
you guard against corner cases.  (Hint: take a look
at ``util.py`` for some useful functions for implementing
training.  Once you've implemented the training function, we can test
it on simple data:

```
>>> h = dt.DT({'maxDepth': 1})
>>> h
Leaf 1

>>> h.train(datasets.TennisData.X, datasets.TennisData.Y)
>>> h
Branch 6
  Leaf 1.0
  Leaf -1.0
```

This is for a simple depth-one decision tree (aka a decision stump).
If we let it get deeper, we get things like:

```
>>> h = dt.DT({'maxDepth': 2})
>>> h.train(datasets.TennisData.X, datasets.TennisData.Y)
>>> h
Branch 6
  Branch 7
    Leaf 1.0
    Leaf 1.0
  Branch 1
    Leaf -1.0
    Leaf 1.0

>>> h = dt.DT({'maxDepth': 5})
>>> h.train(datasets.TennisData.X, datasets.TennisData.Y)
>>> h
Branch 6
  Branch 7
    Leaf 1.0
    Branch 2
      Leaf 1.0
      Leaf -1.0
  Branch 1
    Branch 7
      Branch 2
        Leaf -1.0
        Leaf 1.0
      Leaf -1.0
    Leaf 1.0
```

We can do something similar on the gender data:

```
>>> h = dt.DT({'maxDepth': 2})
>>> h.train(datasets.GenderData.X, datasets.GenderData.Y)
>>> h
Branch 748
  Branch 287
    Leaf 1.0
    Leaf -1.0
  Branch 71
    Leaf -1.0
    Leaf 1.0
```

The problem here is that words have been converted into numeric ids
for features. We can look them up:

```
>>> GenderData.words[748]
'me'
>>> GenderData.words[287]
'love'
>>> GenderData.words[71]
'urllink'
```

(This last one means "contained a URL reference".) Based on this, we
can rewrite the tree (by hand) as:

```
Branch 'me'
  Branch 'love'
    Leaf 1.0
    Leaf -1.0
  Branch 'urllink'
    Leaf -1.0
    Leaf 1.0
```

Now, you should go implement prediction.  This should be easier than
training!  We can test by:

```
>>> runClassifier.trainTestSet(dt.DT({'maxDepth': 1}), datasets.GenderData)
Training accuracy 0.555018, test accuracy 0.553
>>> runClassifier.trainTestSet(dt.DT({'maxDepth': 3}), datasets.GenderData)
Training accuracy 0.589363, test accuracy 0.5725
>>> runClassifier.trainTestSet(dt.DT({'maxDepth': 5}), datasets.GenderData)
Training accuracy 0.616539, test accuracy 0.573
```

Or:

```
>>> runClassifier.trainTestSet(dt.DT({'maxDepth': 1}), datasets.SentimentData)
Training accuracy 0.630833, test accuracy 0.595
>>> runClassifier.trainTestSet(dt.DT({'maxDepth': 3}), datasets.SentimentData)
Training accuracy 0.700833, test accuracy 0.6225
>>> runClassifier.trainTestSet(dt.DT({'maxDepth': 5}), datasets.SentimentData)
Training accuracy 0.759167, test accuracy 0.6275
```

Looks like it does better than the dumb classifiers on training data,
as well as on test data!  Hopefully we can do even better in the
future!

We can use more ``runClassifier`` functions to generate learning
curves and hyperparameter curves:

```
>>> curve = runClassifier.learningCurveSet(dt.DT({'maxDepth': 9}), datasets.GenderData)
[snip]
>>> runClassifier.plotCurve('DT on Gender Data', curve)
```

This plots training and test accuracy as a function of the number of
data points (x-axis) used for training.

**WU2:** We should see training accuracy (roughly) going down and
test accuracy (roughly) going up.  Why does training accuracy tend to
go *down?*  Why is test accuracy not monotonically
increasing?

We can also generate similar curves by chaning the maximum depth
hyperparameter:

```
>>> curve = runClassifier.hyperparamCurveSet(dt.DT({}), 'maxDepth', [1,2,4,8,16,32], datasets.GenderData)
[snip]
>>> runClassifier.plotCurve('DT on Gender Data (hyperparameter)', curve)
```

Now, the x-axis is the value of the maximum depth.

**WU3:** You should see training accuracy monotonically increasing
and test accuracy making a (wavy) hill.  Which of these
is *guaranteed* to happen a which is just something we might
expect to happen?  Why?



## Nearest Neighbors (30%)

To get started with geometry-based classification, we will implement a
nearest neighbor classifier that supports both KNN classification and
epsilon-ball classification.  This should go in ``knn.py``.  The
only function here that you have to do anything about is
the ``predict`` function, which does all the work.

In order to test your implementation, here are some outputs (I suggest
implementing epsilon-balls first, since they're slightly easier):

```
>>> runClassifier.trainTestSet(knn.KNN({'isKNN': False, 'eps': 0.5}), datasets.TennisData)
Training accuracy 1, test accuracy 1
>>> runClassifier.trainTestSet(knn.KNN({'isKNN': False, 'eps': 1.0}), datasets.TennisData)
Training accuracy 0.857143, test accuracy 0.833333
>>> runClassifier.trainTestSet(knn.KNN({'isKNN': False, 'eps': 2.0}), datasets.TennisData)
Training accuracy 0.642857, test accuracy 0.5

>>> runClassifier.trainTestSet(knn.KNN({'isKNN': True, 'K': 1}), datasets.TennisData)
Training accuracy 1, test accuracy 1
>>> runClassifier.trainTestSet(knn.KNN({'isKNN': True, 'K': 3}), datasets.TennisData)
Training accuracy 0.785714, test accuracy 0.833333
>>> runClassifier.trainTestSet(knn.KNN({'isKNN': True, 'K': 5}), datasets.TennisData)
Training accuracy 0.857143, test accuracy 0.833333
```

You can also try it on the digits data:

```
>>> runClassifier.trainTestSet(knn.KNN({'isKNN': False, 'eps': 6.0}), datasets.DigitData)
Training accuracy 0.96, test accuracy 0.64
>>> runClassifier.trainTestSet(knn.KNN({'isKNN': False, 'eps': 8.0}), datasets.DigitData)
Training accuracy 0.88, test accuracy 0.81
>>> runClassifier.trainTestSet(knn.KNN({'isKNN': False, 'eps': 10.0}), datasets.DigitData)
Training accuracy 0.74, test accuracy 0.74

>>> runClassifier.trainTestSet(knn.KNN({'isKNN': True, 'K': 1}), datasets.DigitData)
Training accuracy 1, test accuracy 0.94
>>> runClassifier.trainTestSet(knn.KNN({'isKNN': True, 'K': 3}), datasets.DigitData)
Training accuracy 0.94, test accuracy 0.93
>>> runClassifier.trainTestSet(knn.KNN({'isKNN': True, 'K': 5}), datasets.DigitData)
Training accuracy 0.92, test accuracy 0.92
```

**WU4:** For the digits data, generate train/test curves for
varying values of K and epsilon (you figure out what are good ranges,
this time).  Include those curves: do you see evidence of overfitting
and underfitting?  Next, using K=5, generate learning curves for this
data.

**WU5:** Modify HighD.py appropriately for the following
experiment. The digits (training) data consists of 100 points in 784
dimensions, and lives in the [0,1]<sup>784</sup> hypercube. First,
generate a histogram plot of equivalent, randomly generated data (this
is basically just using HighD.py directly). Next, generate a histogram
of distances computed from DigitData.X. Spend a few sentences
discussing what you see.
