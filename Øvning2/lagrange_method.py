from sympy import symbols, diff, nsolve, Symbol, log

x, y, l = symbols('x, y, l') # Defines the mathematical variable symbols to be used. l is the Lagrangian multiplier 
f = x**2 + y # Insert function f to be maximised/minimised.
g = x-y # Insert constraint function g in the form g(x,y) - constant


def finding_equations(f, g):
    """
    Given the function f and the constraint fucntion g, it returns a list of equations for which the system of equations is going to be solved.
    """
    equations = []
    # here intitiate an empty list (the list of equations to be returned)
    for s in f.atoms(Symbol): #f.atoms(Symbol) picks out the symbols that represent our variables in the function f, i.e. it loops over 'x' and 'y' in this example
        equations.append(f.diff(s) - l*g.diff(s)) 
        # for each s create the correct equation (using diff in sympy), f' + l g', and append to the list with equations
    # append the constraint to the list of equations
    equations.append(g)
    return equations  # returns a list of equations (possibly with a different name), in this case with three items

# nsolve takes a list of equations (determined by finding_equations(f,g) and solves for the given variables. 
# Takes at least three arguments: equations, symbols, starting estimate)

def Task_2():
    print("Task 2")
    result_a = nsolve(finding_equations(f, g), [x, y, l], [1,1,1]) 
    print("Result from first set of equations is:",result_a)

    f_2 = x**2 - 8*x + y**2 - 12*y + 48
    g_2 = x + y - 8

    result_b = nsolve(finding_equations(f_2, g_2), [x, y, l], [1,1,1])
    print("Result from second set of equations is:", result_b)


def Task_3(n):
    print("Task 3")
    variables_string = ["p" + str(i) for i in range(n)]
    variables = []
    for s in variables_string:
        i = symbols(s)
        variables.append(i)

    f_3 = sum([ i * log(i) for i in variables ])
    g_3 = sum(variables) - 1

    variables.append(l)

    result = nsolve(finding_equations(f_3, g_3), variables, [1 for i in range(len(variables))])

    print(f"Result from third set of equations with {n} variables is :", result[:-1])

