# Lab 6: Lagrangians and SVMs

## Lagrangians

In the first part of this lab, we'll play around with Lagrangians.

First, run `saddle_point` in python:

```python
>>> import saddle_point
```

This will generate four figures:

* Figure 1 shows the function we're trying to optimize (a simple quadratic) and the single constraint (x >= 3). Clearly the optimum here is x=3 (by visual inspection).
* Figure 2 shows the Lagrangian. One axis (the one ranging from -8 to +8) is "x". The other axis (ranging from 0 to 10) is alpha. The black line shows the optimal (maximal) value of alpha for any given x; the blue line shows the optimal (minimal) value of x for any given alpha.
* Figure 3 shows the same thing as Figure 2, but as a contour plot instead of a 3D plot
* Figure 4 shows the optimization problem just as a function of alpha. The optimum is clearly at alpha=6, which, in this case, corresponds to x=3.

**QUESTION A:** Spin the 3D figure around so that you're looking at it from the perspective of x. So you see -8..8 on the x-axis and the 0..10 axis is going "away" from you. You should be able to see a saddle point in the black curve where it hits a minimum. For what value of x does it attain that minimum?

Edit the code in `saddle_point.py` so that the constraint is "x >= -2" (rather than the current "x >= 3". You should only have to change line 9. Rerun.

```python
>>> reload(saddle_point)
```

**QUESTION B:** Repeat question A, but for this new figure.

**QUESTION C:** Look at the (new) Figure 4. Where is the optimum for alpha? What does this tell you about the constraint in the constrained optimization?


## SVMs

In the second part of the lab, we'll play around with SVMs and kernels
to get a sense of what they are actually doing. In order to use this, you'll have to install [libsvm](https://www.csie.ntu.edu.tw/~cjlin/libsvm/). If you don't have svm-train, but do have sklearn, replace `svm-train ...` below with `python svm-train.py ...` and my wrapper will attempt to do a crummy job of mimicing svm-train.

We can start by training a simple linear SVM:

```
% svm-train -t 0 -c 100 data0 data0.model
% python drawBoundary.py data0
```

This invocation of svm-train says:

    -t 0    -- use a linear kernel
    -c 100  -- set "C" = 100, which means "overfit a lot"

This is an easily separable dataset, which is reflected by the small
number of support vectors. In the plot, the SVs are drawn big (and are
on the margin, the dashed line one unit away from the decision
boundary, the solid line).

**QUESTION A:** You should have found that it takes 3 support
vectors. Could you have fewer (eg., 2) support vectors here?

Although it's unnecessary, we can also train a polynomial SVM with
degree 10 (for instance), with:

```
% svm-train -t 1 -r 1 -d 10 -c 100 data0 data0.model
% python drawBoundary.py data0
```

This says:

    -t 1      -- use a polynomial kernel
    -r 1      -- use (1 + u*v)^degree, where "r" is the "1"
    -d 10     -- tenth degree

You'll see that you get a curved decision boundary, though of course
this is somewhat overkill.

```
% svm-train -t 2 -c 100 -g 1 data0 data0.model
% python drawBoundary.py data0
```

(Here, `-t 2` means RBF and `-g 1` means gamma=1)

Again, this is overkill. But we can try to understand RBF kernels a
bit better by "turning up" the gamma:

```
% svm-train -t 2 -c 100 -g 100 data0 data0.model
% python drawBoundary.py data0
```

A gamma of 100 means that you have to be *really* close to a point to
have a kernel value that's non-zero.

**QUESTION B:** why do you get these little blobs? How high do you have
   to turn gamma up in order to get a little decision boundary around
   each example?

-----

Let's now switch to a more complex dataset. We'll begin by failing
with a linear model:

```
% svm-train -t 0 -c 100 data1 data1.model
% python drawBoundary.py data1
```

As you can see, this data fails horribly.

**QUESTION C:** There are a lot of red support vectors on the blue side
   of the decision boundary. Why?

However, now we can get some mileage out of polynomial kernels:

```
% svm-train -t 1 -r 1 -d 3 -c 100 data1 data1.model
% python drawBoundary.py data1
```

**QUESTION D:** based on this data, is the 0/1 loss on the training
   data zero? Is the hinge loss on the training data zero?

**QUESTION E:** train an RBF kernel on this data. What's the smallest
   gamma for which you can get a good decision boundary?

