from math import log

def stirling(n):
    """
    Returns ln n! using Stirling's approximation
    """
    return n*log(n) - n

def exact_sol(n):
    """
    Returns ln n! exactly
    Why is factorial not imported above?
    """
    return sum([log(i) for i in range(1, n+1)]) 

n = [5, 10, 100, 10**3, 10**4, 10**5, 10**6] #Fill in the values of n that you wish to test, e.g. in the range from 5 to 10^6
with open("./Øvning3/stirling.txt", "w") as f: # Creates and opens the file 
    f.write('{:>12} {:>16} {:>18} {:>18} {:>18}'.format('n', 'Exact', 'Stirling', 'Absolute error', 'Relative error') + '\n')
    for i in n:
        ex = exact_sol(i)
        st = stirling(i)
        f.write('{:12d} {:16.4f} {:18.4f} {:18.4f} {:18.4f}'.format(i, ex, st, ex-st, 1-st/ex) + '\n') 
