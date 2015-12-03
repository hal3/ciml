# CMSC 422 Project 3: Unsupervised Learning

In this project, we will explore dimensionality reduction (PCA) and
clustering. Finally, you should do something fun that *demonstrates
that you actually learned something in this class*!

Files you'll edit:

    dr.py           Implementation of PCA
    clustering.py   Implementation of K-means (and variants)

Files you might want to look at:

    datasets.py     Some simple toy data sets
    digits          Digits data
    util.py         Utility functions, plotting, etc.

## PCA *[30%]*

Our first tasks are to implement PCA.  If implemented correctly, these
should be 5-line functions (plus the supporting code I've provided):
just be sure to use numpy's eigenvalue computation code.  Implement
PCA in the function `pca` in `dr.py`.

Our first test of PCA will be on Gaussian data with a known covariance
matrix.  First, let's generate some data and see how it looks, and see
what the *sample covariance* is:

```python
>>> Si = util.sqrtm(array([[3,2],[2,4]]))
>>> x = dot(randn(1000,2), Si)
>>> plot(x[:,0], x[:,1], 'b.')
>>> dot(x.T,x) / real(x.shape[0])
array([[ 2.88360146,  2.05144774],
       [ 2.05144774,  4.05987148]])
```

(Note: The reason we have to do a matrix square-root on the covariance
is because Gaussians are transformed by standard deviations, not by
covariances.)

Note that the sample covariance of the data is almost exactly the true
covariance of the data.  If you run this with 100,000 data points
(instead of 1000), you should get something even closer to
`[[3,2],[2,4]]`.

Now, let's run PCA on this data.  We basically know what should
happen, but let's make sure it happens anyway.

```python
>>> (P,Z,evals) = dr.pca(x, 2)
>>> Z
array([[-0.60270316, -0.79796548],
       [-0.79796548,  0.60270316]])
>>> evals
array([ 5.72199341,  1.45051781])
```

This tells us that the largest eigenvalue corresponds to the
direction `[-0.603, -0.798]` and the second largest corresponds to
the direction `[-0.798, 0.603]`.  We can project the data onto
the first eigenvalue and plot it in red, and the second eigenvalue in
green.  (Unfortunately we have to do some ugly reshaping to get
dimensions to match up.)

```python
>>> x0 = dot(dot(x, Z[:,0]).reshape(1000,1), Z[:,0].reshape(1,2))
>>> x1 = dot(dot(x, Z[:,1]).reshape(1000,1), Z[:,1].reshape(1,2))
>>> plot(x[:,0], x[:,1], 'b.', x0[:,0], x0[:,1], 'r.', x1[:,0], x1[:,1], 'g.')
```

IGNORE THIS QUESTION: **WU1:** Depending exactly on your random data, one or more of these
lines might not pass exactly through the data as we would like it to.
Why not?

Now, back to digits data.  Let's look at some "eigendigits."

```python
>>> (X,Y) = datasets.loadDigits()
>>> (P,Z,evals) = dr.pca(X, 784)
>>> evals
array([ 0.05465988,  0.04320249,  0.03914405,  0.03072822, 0.02969435, .....
```

(Warning: this takes about a minute to compute for me.)  Eventually
the eigenvalues drop to zero.

**WU2:** Plot the normalized eigenvalues (include the plot in your
writeup).  How many eigenvectors do you have to include before you've
accounted for 90% of the variance?  95%?  (Hint: see function
`cumsum`.)

Now, let's plot the top 50 eigenvectors:

```python
>>> util.drawDigits(Z.T[:50,:], arange(50))
>>> show(False)
```

**WU3:** Do these look like digits?  Should they?  Why or why not?
(Include the plot in your write-up.)


## K-Means Clustering *[40%]*

Your second task is to implement the largest distance heuristic for
kmeans clustering in `clustering.py`.

We'll now quickly run through some basic experiments k-means:

```python
>>> mu0 = clustering.initialize_clusters(datasets.X2d, 2, 'determ')
>>> (mu,z,obj) = clustering.kmeans(datasets.X2d, mu0)
>>> mu
array([[ 2.31287961,  1.51333813],
       [-2.13455999, -2.15661017]])
>>> z
array([0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0,
       1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1])
>>> obj
array([ 1.91484251,  1.91484251])
```

**Hint:** While running, this will plot the results.  If you want
to turn that off, comment out the obvious line in the `kmeans`
function.  Plus, when it says "Press enter to continue", if you type
"q" and press enter, it will stop bugging you.

You can also play with another example:

```python
>>> mu0 = clustering.initialize_clusters(datasets.X2d2, 4, 'determ')
>>> (mu,z,obj) = clustering.kmeans(datasets.X2d2, mu0)
Iteration 0, objective=5.84574
Iteration 1, objective=4.3797
Iteration 2, objective=3.06938
Iteration 3, objective=2.45218
Iteration 4, objective=2.34795
Iteration 5, objective=2.34795
>>> mu
array([[ 3.06150611, -1.07977065],
       [-3.92433223,  1.99052827],
       [ 0.87252863,  4.63384851],
       [-3.17087245, -4.10528255]])
>>> z
array([3, 1, 2, 3, 0, 1, 1, 2, 2, 0, 3, 0, 0, 0, 2, 3, 3, 3, 0, 0, 1, 0, 0,
       0, 2, 2, 0, 0, 0, 1, 0, 3, 3, 2, 2, 2, 1, 1, 3, 0, 3, 0, 0, 3, 1, 3,
       3, 2, 1, 0, 1, 1, 3, 2, 3, 3, 0, 0, 3, 2, 0, 3, 1, 3, 0, 3, 2, 3, 3,
       3, 3, 3, 0, 1, 0, 3, 0, 0, 1, 2, 3, 2, 2, 3, 3, 1, 2, 0, 0, 2, 3, 0,
       1, 3, 0, 2, 3, 3, 3, 3, 2, 2, 3, 1, 0, 3, 0, 0, 0, 0, 0, 1, 1, 2, 0,
       1, 0, 2, 3, 1, 3, 0, 1, 1, 3, 0, 0, 1, 0, 3, 3, 1, 0, 0, 3, 0, 2, 2,
       1, 0, 2, 3, 3, 3, 0, 3, 2, 3, 1, 1, 0, 2, 1, 3, 3, 0, 2, 0, 2, 0, 1,
       2, 3, 1, 0, 3, 0, 3, 3, 2, 2, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 2, 3, 0,
       0, 0, 2, 3, 2, 0, 2, 0, 0, 3, 0, 2, 0, 1, 2, 3, 3, 0, 3, 3, 2, 3, 1,
       0, 0, 0, 0, 3, 0, 0, 1, 0, 3, 0, 1, 2, 3, 2, 3, 3, 1, 3, 3, 3, 1, 3,
       0, 3, 2, 0, 2, 3, 2, 3, 3, 1, 3, 3, 3, 3, 2, 3, 0, 2, 2, 0, 0, 2, 1,
       2, 3, 1, 3, 1, 3, 1, 3, 0, 1, 3, 3, 0, 3, 0, 1, 3, 3, 1, 2, 3, 0, 2,
       3, 0, 0, 3, 3, 1, 2, 3, 0, 3, 3, 1, 1, 1, 2, 0, 3, 0, 3, 1, 0, 3, 3,
       0])
>>> obj
array([ 5.84574233,  4.37970445,  3.06937814,  2.45218374,  2.34795137,
        2.34795137])
```

Once you've implemented the furthest first heuristic, you can do an
 test by:

```python
>>> (X,Y) = datasets.loadDigits()
>>> mu0 = clustering.initialize_clusters(X, 10, 'ffh')
>>> (mu,z,obj) = clustering.kmeans(X, mu0, doPlot=False)
>>> plot(obj)
>>> show(block=False)
>>> util.drawDigits(mu, arange(10))
```

(This takes a while to run for me: about 30 seconds total.)

Note: it's very hard to provide test cases for this because of
randomness and python (unfortunately) doesn't guarantee cross-platform
randomness to be the same. Here's what I can do; hopefully it's
somewhat useful.

```python
>>> for rep in range(10):
...     np.random.seed(1234 + rep)
...     mu0 = clustering.initialize_clusters(X, 10, 'ffh')
...     (mu,z,obj) = clustering.kmeans(X, mu0, doPlot=False)
...     finalObj.append(obj[-1])

(lots of output)

>>> np.mean(finalObj)
0.44031610993896342
```

**WU4:** Run kmeans with ffh.  How many iterations does it seem to
take for kmeans to converge using ffh?  Do the resulting cluster means
look like digits for most of these runs?  Pick the "best" run (i.e.,
the one with the lowest final objective) and plot the digits (include
the plot in the writeup).  How many of the digits 0-9 are represented?
Which ones are missing?  Try both with ffh and with random
initialization: how many iterations does it take for kmeans to
converge (on average) for each setting?

**WU5:** Repeat WU4, but for k=25.  Pick the best of 5 runs, and
plot the digits.  Are you able to see all digits here?

Finally, implement the kmeans++ heuristic. Here is some output:

```python
>>> for rep in range(10):
...     np.random.seed(1234 + rep)
...     mu0 = clustering.initialize_clusters(X, 10, 'km++')
...     (mu,z,obj) = clustering.kmeans(X, mu0, doPlot=False)
...     finalObj.append(obj[-1])

(lots of output)

np.mean(finalObj)
0.43999423428294626
```
**WU6:** Compare vanilla kmeans (with random initialization) to ffh to km++ for (a) a small number of clusters (say, 2 or 3) and (b) a large number of clusters (say 25). Do you see a big difference in performance at either end?

## Choose your own adventure *[30%]*

**WU7:** As a warm up, complete lab 6 and include the answers to questions in
that lab here.

Now, go out and find some data that seems interesting in some way. You
can either grab some data that wasn't meant to be used as a learning
problem (like the wine data I downloaded for one of the earlier labs)
or some data that is "obviously" a learning problem. If you want some
pointers to places where you might find interesting data, look at:
data.gov, healthdata.gov, or www.people-press.org/category/datasets or
try to find something else. Be creative and find something you think
would be cool (there are some other ideas at the end below). If you
need help, talk to one of the instructors. (Note: you *must* do
something more complicated than binary classification.)

Once you've defined your learning problem, find a good tool for
solving it. You can use libsvm, sklearn, keras, caffe or anything
else. (Just be sure to give appropriate credit in your writeup.) Build
an appropriate learner using anything you've learned in class. In
particular, split the data into train/dev/test and tune hyperparamters
(C, kernel and kernel parameters) on the dev data, and report final
results on the test data. Do appropriate hyperparameter tuning. 

**WU11**: write one page describing what you did for this section. Be
sure to answer the following questions: (a) what is your data and why
did you choose it? (b) what ML solution did you choose and, most
importantly, *why* was this ap appropriate choice? (c) how did you
choose to evaluate success? (d) what software did you use and why did
you choose it? (e) what are the results? (f) show some examples from
the development data that your approach got correct and some it got
wrong: if you were to try to fix the ones it got wrong, what would you
do?

For grading: I don't care how well your approach did. I'm only
interested in whether you chose a reasonable approach for the problem,
are evaluating it in a reasonable way, and that you have done a
reasonable error analysis (f).
