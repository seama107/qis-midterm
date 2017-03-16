# qis-midterm

**Author:** Michael Seaman

**Due date:** 2017/03/17

## Specification

Hi all,
Next week please complete the following coding project in python,
due at the end of Friday by email.
Simulate the output of a CHSH Bell test, with tunable angles.
That is:
* Start with a 2-qubit Bell state:  |Phi^+> = (|00> + |11>)/sqrt(2)
* Have the first qubit measure a tunable observable O(theta1) with
eigenstate |theta1> = cos(theta1/2)|0> + sin(theta1/2)|1>
corresponding to eigenvalue +1, and eigenstate |theta1p> =
-sin(theta1/2)|0> + cos(theta1/2)|1> corresponding to the
eigenvalue -1.
* Have the second qubit measure a similar
observable O(theta2). However, rather than computing the
expectation values directly, generate the observed random
data. (See next bullet.)

* Done properly, each single measurement should return only two
observed eigenvalues as a tuple, e.g., (+1,+1), such that a large
number of random samples converges to the correct statistics
predicted by the state. You will need to compute the correct
probabilities from the state for each observation, so that you
may randomly sample from the correct probability distribution.
[An easy way to do this is to sample a random float from the
interval [0,1] and compare that float to the outcome
probabilities. i.e., if that random float is less than P(-1,-1)
then return (-1,-1), else if that random float is less than
P(-1,-1)+P(-1,+1) then return (-1,+1), else if that random float
is less than P(-1,-1)+P(-1,+1)+P(+1,-1) then return (+1,-1),
otherwise return (+1,+1).]

* Verify the correctness of your measurement implementation by
generating a large set of measured data and showing that its
average approximates the correct analytic expectation value of
the product observable O(theta1)O(theta2).
* Generate data for the CHSH correlator. That is, generate data for
4 separate ensembles corresponding to the observable pairs  
A=O(0)O(pi/4), B=O(0)O(-pi/4), C=O(pi/2)O(pi/4),
D=O(pi/2)O(-pi/4). Each ensemble of data should just be
collections of random +1 and -1 values that were observed on each
trial. Show that averaging the data for each observable
separately produces seemingly reasonable results, but when those
averages are added together according to the CHSH prescription
(with one relative negative sign) then the total sum exceeds the
classically expected bound of 2 and converges to the quantum
upper bound of 2sqrt(2).

* Plot the result of the simulated correlator as a function of an
added tunable angle phi for only the second qubit observable,
such that the usual CHSH observables correspond to phi = 0.  That
is: A(phi)=O(0)O(pi/4+phi), B(phi)=O(0)O(-pi/4+phi),
C(phi)=O(pi/2)O(pi/4+phi), D(phi)=O(pi/2)O(-pi/4+phi).
* Compare your simulated results to what is expected from an analytical calculation of the correlator as a function of phi.
Range from phi=0 to phi=2pi in increments of pi/16.

You should turn in 1 python module (.py file) with your
implementation, and 1 Jupyter notebook (.ipynb file) that
demonstrates your working implementation and shows supporting
plots.


## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

Michael Seaman
