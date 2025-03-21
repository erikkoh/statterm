from sympy import diff, symbols, solve, plot

eps, sig, r = symbols('eps sig r')

#Removing # from eps and sig below will turn eps and sig into normal variables  of python symbols.
eps = 0.997 #kj/mol
sig = 3.4 #Å

V = 4*eps*((sig/r)**12-(sig/r)**6)#Input expression for the potential

#calculate Fr using diff()

Fr = -diff(V, r)

# Recall that the force is minus the gradient of the potential energy
print("Fr is: ", Fr)
print(solve(Fr, r)) # to get where the force is zero
print(solve(V, r)) # to get where the potential is

plot(Fr, V, (r, 0, 10), xlabel='Distance', ylabel='Force', axis_center=(0,0), ylim=(-3*eps,4*eps), legend=True)
