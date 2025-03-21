from sympy import diff, latex, symbols, plot

r = symbols('r')

eps = 1 #Fill in a value for epsilon
sig = 1 #Fill in a value for sigma

V = 4*sig*((eps/r)**12-(eps/r)**6)#Fill in a value for Lennard-Jones potential

plot(V, (r, 0, 10), xlabel='Distance', ylabel='Potential', axis_center=(0,0), ylim=(-eps,4*eps))
