# Lab 2: KNN and High Dimensional Data

In this lab, we'll look at high dimensional data and explore using KNN
for classification (no K-means for now).

## TASK 1: PLAYING WITH HIGH-D DATA

If you have numpy and matplotlib correctly installed, you should be
able to run:

% python HighD.py 

and get a picture of five histograms. Open up HighD.py to understand
what's being plotted. Essentially, we are generated 200 random points
in D dimensions (where D is being varied) and computing pairwise
distances between these points.

(A) As the dimensionality increases, do the distances between pairs of
points become more or less concentrated around a single value?

(B) In the code, instead of plotting distance on the x-axis, we're
plotting (distance/sqrt(D)). Why is this the right thing to do?

## TASK 2: CLASSIFYING DIGITS

Our first task will be to use KNN to classify digits. In other words,
we get an image of a hand-drawn digit (28x28 pixels, greyscale), and
have to decide what digit is is. To make life simpler, we'll consider
only the binary classification version, in two setups: (A)
distinguishing ONEs from TWOs and (B) distinguishing TWOs from
THREEs.

(A) In the data directory, you'll find two .png files that show the
training data. Open them up. Are there any that you, as a human, have
difficulty distinguishing (if so, list the row/column, where 0,0 is
the upper left and 9,9 is the bottom right). Which of these (1vs2 or
2vs3) do you expect to be a harder classification problem?

(B) Let's verify that KNN does very well on training data. Run the
following:

% python KNN.py data/1vs2.tr data/1vs2.tr 1

0.0

This says "do KNN, with 1vs2.tr as the training data and
1vs2.tr as the testing data, using K=1." The 0.0 is the error rate,
which is zero. Verify the same thing for 2vs3.tr

(C) The KNN.py implementation will let you specify multiple values for
K and get error rates for all of them. In particular, you can say
something like:

% python KNN.py data/1vs2.tr data/1vs2.tr 1 5 10 25 50 100

0.0	0.08	0.12	0.16	0.28	0.5

This runs the same thing for six values of K (1, 5, ..., 100) and
prints the respective error rates. Notice that for K=100 the error
rate is 50% -- why does this happen?

(D) Repeat the same exercise, this time evaluating on the development
data, and using odd values of K ranging from 1 to 21. Do this for both
1vs2 and 2vs3. Which one is harder? For each, what is the optimal
value of K? (In the case of ties, how would you choose to break ties?)

(E) Now, go edit KNN.py. This might take a bit of effort since you'll
have to figure out what it's doing. But the function I want you to
look at is "classifyKNN." This takes D (the training data) and knn
(the list of the K nearest neighbors, together with their
distances). It iterates over each of the (dist,n) nearest
neighbors. Here, dist is the distance and n is the training example
id, so D[n] is the corresponding training example. It then "votes"
this into a prediction yhat.

Modify this function so that each example gets a weighted vote, where
its weight is equal to exp(-dist). This should be a one- or two-liner.

Rerun the same experiments as in (D). Does this help or hurt? What do
you observe as K gets larger and _WHY_ do you observe this?

If you want to play around, try exp(-dist / CONSTANT) where CONSTANT
now is a hyperparameter. What happens as CONSTANT tends toward zero?
Tends toward infinity?

# TASK 3: OPTIONAL: RANDOM versus DIGITS data in high dimensions

If you've gotten this far, congratulations! This task is taken
directly out of project 1, so you can do it now if you like, or you
can wait to do it for the project. (It literally appears verbatim
there.) Student's choice!

The goal here is to look at whether what we found for uniformly random
data points holds for naturally occurring data (like the digits data)
too! We must hope that it doesn't, otherwise KNN has no hope of
working, but let's verify.

The problem is: the digits data is 784 dimensional, period, so it's
not obvious how to try "different dimensionalities." For now, we will
do the simplest thing possible: if we want to have 128 dimensions, we
will just select 128 features randomly.

This is your task, which you can accomplish by munging together
HighD.py and KNN.py and making appropriate modifications.

A. First, get a histogram of the raw digits data in 784
dimensions. You'll probably want to use the `exampleDistance` function
from KNN together with the plotting in HighD.

B. Extend `exampleDistance` so that it can subsample features down to
some fixed dimensionality. For example, you might write
`subsampleExampleDistance(x1,x2,D)`, where `D` is the target
dimensionality. In this function, you should pick `D` dimensions at
random (I would suggest generating a permutation of the number
[1..784] and then taking the first D of them), and then compute the
distance but _only_ looking at those dimensions.

C. Generate an equivalent plot to HighD with D in [2, 8, 32, 128, 512]
but for the digits data rather than the random data. Include a copy of
both plots and describe the differences.
