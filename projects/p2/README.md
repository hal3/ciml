# Project 2: Multiclass and Linear Models

There are two parts to this project. The first is to play around with multiclass reductions. The second is to play around with linear models.

## Multiclass Classification *[30% impl, 20% writeup]*

In this section, you will explore the differences between three
multiclass-to-binary reductions: one-against-all (OVA), all-versus-all
(AVA) and a tree-based reduction (TREE).  This is largely based
on LAB4, and the evaluation will be on the quizbowl question answering
dataset that we used recently to beat Ken Jennings.

First, you must implement AVA (the `multiclass.py` file that comes
with this project is identical to the one from the lab, except the
existence of the extra class for trees). Second, you must implement a
tree-based reduction. Most of train is given to you, but predict you
must do all on your own. I've provided a tree class to help you:

```python
>>> t = multiclass.makeBalancedTree(range(6))
>>> t
[[0 [1 2]] [3 [4 5]]]
>>> t.isLeaf
False
>>> t.getLeft()
[0 [1 2]]
>>> t.getLeft().getLeft()
0
>>> t.getLeft().getLeft().isLeaf
True
```

**WU1 (10%):** From LAB4, Answer A, B, C for both OVA and AVA.

**WU2 (10%):** Using decision trees of constant depth for each
classifier (but you choose it as well as you can!), train AVA, OVA and
Tree (using balanced trees) for the wine data. Which does best?

**ExtraCredit (10%):** Build a better tree (any way you want) other
than the balanced binary tree. Fill in your code for this in
`getMyTreeForWine`, which defaults to a balanced tree. It should get
at least 5% lower error to get the extra credit. WU: describe what you
did.


## Gradient Descent and Linear Classification *[30% impl, 20% writeup]*

To get started with linear models, we will implement a generic
gradient descent methods.  This should go in `gd.py`, which
contains a single (short) function: `gd` This takes five
parameters: the function we're optimizing, it's gradient, an initial
position, a number of iterations to run, and an initial step size.

In each iteration of gradient descent, we will compute the gradient
and take a step in that direction, with step size `eta`.  We
will have an *adaptive* step size, where `eta` is computed
as `stepSize` divided by the square root of the iteration
number (counting from one).

Once you have an implementation running, we can check it on a simple
example of minimizing the function `x^2`:

```python
>>> gd.gd(lambda x: x**2, lambda x: 2*x, 10, 10, 0.2)
(1.0034641051795872, array([ 100.        ,   36.        ,   18.5153247 ,   10.95094653,
          7.00860578,    4.72540613,    3.30810578,    2.38344246,
          1.75697198,    1.31968118,    1.00694021]))
```

You can see that the "solution" found is about 1, which is not great
(it should be zero!), but it's better than the initial value of ten!
If yours is going up rather than going down, you probably have a sign
error somewhere!

We can let it run longer and plot the trajectory:

```python
>>> x, trajectory = gd.gd(lambda x: x**2, lambda x: 2*x, 10, 100, 0.2)
>>> x
0.003645900464603937
>>> plot(trajectory)
>>> show(False)
```

It's now found a value close to zero and you can see that the
objective is decreasing by looking at the plot.

**WU3 (5%):** Find a few values of step size where it converges and
a few values where it diverges.  Where does the threshold seem to
be?

**WU4 (10%):** Come up with a *non-convex* univariate
optimization problem.  Plot the function you're trying to minimize and
show two runs of `gd`, one where it gets caught in a local
minimum and one where it manages to make it to a global minimum.  (Use
different starting points to accomplish this.)

If you implemented it well, this should work in multiple dimensions,
too:

```python
>>> x, trajectory = gd.gd(lambda x: linalg.norm(x)**2, lambda x: 2*x, array([10,5]), 100, 0.2)
>>> x
array([ 0.0036459 ,  0.00182295])
>>> plot(trajectory)
```

Our generic linear classifier implementation is
in `linear.py`.  The way this works is as follows.  We have an
interface `LossFunction` that we want to minimize.  This must
be able to compute the loss for a pair `Y` and `Yhat`
where, the former is the truth and the latter are the predictions.  It
must also be able to compute a gradient when additionally given the
data `X`.  This should be all you need for these.

There are three loss function stubs: `SquaredLoss` (which is
implemented for you!), `LogisticLoss` and `HingeLoss`
(both of which you'll have to implement.  My suggestion is to hold off
implementing the other two until you have the linear classifier
working.

The `LinearClassifier` class is a stub implemention of a
generic linear classifier with an l2 regularizer.  It
is *unbiased* so all you have to take care of are the weights.
Your implementation should go in `train`, which has a handful
of stubs.  The idea is to just pass appropriate functions
to `gd` and have it do all the work.  See the comments inline
in the code for more information.

Once you've implemented the function evaluation and gradient, we can
test this.  We'll begin with a very simple 2D example data set so that
we can plot the solutions.  We'll also start with *no
regularizer* to help you figure out where errors might be if you
have them.  (You'll have to import `mlGraphics` to make this
work.)

```python
>>> f = linear.LinearClassifier({'lossFunction': linear.SquaredLoss(), 'lambda': 0, 'numIter': 100, 'stepSize': 0.5})
>>> runClassifier.trainTestSet(f, datasets.TwoDAxisAligned)
Training accuracy 0.91, test accuracy 0.86
>>> f
w=array([ 2.73466371, -0.29563932])
>>> mlGraphics.plotLinearClassifier(f, datasets.TwoDAxisAligned.X, datasets.TwoDAxisAligned.Y)
>>> show(False)
```

Note that even though this data is clearly linearly separable,
the *unbiased* classifier is unable to perfectly separate it.

If we change the regularizer, we'll get a slightly different
solution:

```python
>>> f = linear.LinearClassifier({'lossFunction': linear.SquaredLoss(), 'lambda': 10, 'numIter': 100, 'stepSize': 0.5})
>>> runClassifier.trainTestSet(f, datasets.TwoDAxisAligned)
Training accuracy 0.9, test accuracy 0.86
>>> f
w=array([ 1.30221546, -0.06764756])
```

As expected, the weights are *smaller*.

Now, we can try different loss functions.  Implement logistic loss and
hinge loss.  Here are some simple test cases:

```python
>>> f = linear.LinearClassifier({'lossFunction': linear.LogisticLoss(), 'lambda': 10, 'numIter': 100, 'stepSize': 0.5})
>>> runClassifier.trainTestSet(f, datasets.TwoDDiagonal)
Training accuracy 0.99, test accuracy 0.86
>>> f
w=array([ 0.29809083,  1.01287561])

>>> f = linear.LinearClassifier({'lossFunction': linear.HingeLoss(), 'lambda': 1, 'numIter': 100, 'stepSize': 0.5})
>>> runClassifier.trainTestSet(f, datasets.TwoDDiagonal)
Training accuracy 0.98, test accuracy 0.86
>>> f
w=array([ 1.17110065,  4.67288657])
```

**WU5 (5%):** For each of the loss functions, train a model on the
binary version of the wine data (called WineDataBinary) and evaluate
it on the test data. You should use lambda=1 in all cases. Which works
best? For that best model, look at the learned weights. Find
the *words* corresponding to the weights with the greatest
positive value and those with the greatest negative value (this is
like LAB3). Hint: look at WineDataBinary.words to get the id-to-word
mapping. List the top 5 positive and top 5 negative and explain.

## Classification with Many Classes *[0% -- just extra credit]*

Finally, we'll do multiclass classification using Scikit-learn functionality. You should look in `quizbowl.py` for a stub here.

Here's an example question from the development data:

    This man and Donald Bayley created a secure voice communications machine called "Delilah".
    The Chinese Room Experiment was developed by John Searle in response to one of this man's namesake tests.
    He showed that the halting problem was undecidable.
    He devised a bombe with Gordon Welchman that found the settings of an Enigma machine.
    One of this man's eponymous machines which can perform any computing task is his namesake "complete."
    Name this man, whose eponymous test is used to determine if a machine can exhibit behavior indistinguishable from that of a human.

The point is that the more of the question you get, the easier the problem becomes.

(More help is available here: http://scikit-learn.org/stable/modules/multiclass.html)

The default code in there just runs OAA and AVA on top of a linear SVM. If you just run `quizbowl.py`, you will get output like the following (takes a minute or two on my machine).

```
RUNNING ON EASY DATA

training oaa
predicting oaa
error = 0.293413
training ava
predicting ava
error = 0.218563


RUNNING ON HARD DATA

training oaa
predicting oaa
error = 0.592814
training ava
predicting ava
error = 0.553892
```

This is running on a shrunken version of the data (that only contains answers that occur at least 20 times in the data).

The first ("easy") version is when you get to see the entire question. The second ("hard") version is when you only get to use the first two sentences. It's clearly significantly harder!

Your task is to do as well as you can on either the small data or the large data. There will be two separate leaderboards. You get 5% extra credit for tying my system (Hal9000) on *either* dataset (small or large), and then another 5% if you're the first place team, 3% second and 1% third. The script `quizbowl.py` includes a command in the last line that sames predictions to a text file: that's what you upload for the EC.

You're free to do anything you want, but you must include a writeup that says what you did.
