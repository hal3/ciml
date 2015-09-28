# Lab 3: Evaluation and Significance

Today's lab is about evaluating learning algorithm. I've provided the
true labels from last year's P1 "last part" assignment (note: it was a
different task), and the solutions produced by the top three
teams.

You can start by loading ``eval.py`` into a python shell. This will
load in the true labels to the variable ``Y`` and the top three
solutions into ``allP[0]``, ``[1]`` and ``[2]``, respectively (0 is
the "winner").

A) Compute the accuracies of these three solutions. This should be a
one-linear in python using numpy. The labels are 0 or 1, and the
predicted values are all between 0 and 1. You should treat anything
over 0.5 as "1" and <=0.5 as "0". Hint: look at np.average or
np.mean. If you cannot do it in one line (think about it first!) ask
me.

You can draw precision/recall curves for this data using:

```python
>>> makeManyCurves(Y,allP)
```

In this, the X-axis is precision and the Y-axis is recall. This is
obtained by varying the threshold away from 0.5.

B) Does a high threshold lead to high precision and low recall or high
recall and low precision? What about a low threshold?

Sometimes you care about high precision systems. For instance, I might
say "if I require a precision of at least 0.75, how high of a recall
can I get? This means that I want a system that, when it says "yes"
it's right 75% of the time... what percentage of the true "yes"
answers can I find.

C) This measure is called "recall at P=0.75" -- what is it
(approximately) for the three curves?

I've given you a partial implementation of the ttest, but you'll need
to fill in some of the details. Once you've done that, you can run
something like:

```python
>>> ttest(Y, allP[1], allP[0])
(4.1490355592633517, 'significant at 99.5% level')
```

This says that the first place team is better than the second place
team with 99.5% confidence.

```python
>>> ttest(Y, allP[2], allP[1])
(0.20950326198721958, 'not significant at 90% level')
```

This says that the second place team is not significantly better than
the third place team, even at 90%.

Now, if you have less data, you are often less likely to be able to
tease apart significant differences. We can force the ttest to run on
a subset of the data:

```python
>>> ttest(Y, allP[1], allP[0], restrictTo=500)
(0.88445909887276331, 'not significant at 90% level')

>>> ttest(Y, allP[1], allP[0], restrictTo=750)
(2.0814897135353521, 'significant at 97.5% level')
```

You can plot the t-statistic as a function of the amount of data
using:

```python
>>> plt.plot([ttest(Y,allP[1],allP[0], i)[0] for i in range(10160)])
>>> plt.show()
```

(There will be a couple warnings that you can ignore.)

D) Based on this, how much data do you need to get 95% significance?
99.5% significance? 

E) You'll note that this is not a monotonically increasing
function. Why does this happen? What does it mean from the perspective
of testing significance?

