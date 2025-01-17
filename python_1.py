#Task 5
from sympy import symbols, log

x, y = symbols('x,y')

f = 3*x**2

g = log(x)

h = x**3+2*y**2

print(f.diff(x))
print(g.diff(x))
print([h.diff(x),h.diff(y)])
