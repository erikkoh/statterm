import numpy as np
from sympy.utilities.iterables import multiset_permutations
import matplotlib.pyplot as plt
import pickle

def get_lattice_shape(n): 
    """
    Determines the lattice shapes that will be used in this exercise, given n particles.
    """
    shapes = {4:(2,2), 6:(2,3), 8:(2,4), 12:(3,4), 16:(4,4), 20:(5,4), 24:(6,4)}
    return shapes[n]

def count_AB(lattice): 
    """
    Returns the number of AB-interactions, n_AB, for a provided lattice.
    Uses periodic boundary conditions.
    """
    n_AB = 0 
    shape = lattice.shape
    # Can np.ndenumerate be useful? Need both the coordinates of the lattice point and its value.
    # How do you avoid double counting? Only look at neighbours to A (or neighbours to B)
    for coord, particle in np.ndenumerate(lattice): # ADD your code 
        if particle == 'A': #Prevents double counting
            # loop over the number of possible neighbours
            for incr in [(1,0),(0,-1),(-1,0),(0,1)]: # neighbour increments
                # The modulo operation ensures that periodic boundary conditions are employed
                # neighbour needs to be a tuple
                neighbour = tuple([(coord[0] + incr[0]) % shape[0], (coord[1] + incr[1]) % shape[1]])  # ADD your code
                if lattice[neighbour] == 'B': #Checks if AB-interaction
                    n_AB += 1 
    return n_AB
    
def create_arrays_and_count(n): 
    """
    Given the number of molecules/lattice points, n, and returns a list with the number of AB interactions for all microstates, m_AB.
    A condition is that the number of A and B molecules is equal.
    """
    m_AB = []
    lattice_shape = get_lattice_shape(n)
    # What does e.g. multiset_permutations(2*'AB') give?
    for config in multiset_permutations(int(n/2)*"AB"): # ADD your code 
        # Here, convert config to a numpy array and convert to a lattice (using np.reshape and lattice_shape above) 
        # Then count the number of AB interactions using the function count_AB
        config = np.array(list(config)).reshape(lattice_shape)
        number_of_ab = count_AB(config)
        m_AB.append(number_of_ab)
    return m_AB

for i in [4, 6, 8, 12, 16, 20, 24]: # The system sizes, shorten the list while testing 
    m_AB = create_arrays_and_count(i) 
    macrostates = sorted(list(set(m_AB))) # Sorts the macrostates list in ascending order
    # Find degeneracies by counting the number of times a certain number of bonds appear in m_AB
    degeneracies = [sum( 1 for i in m_AB if i == j) for j in macrostates]# ADD your code
    #Plots bar chart
    y_pos = np.arange(len(macrostates))
    print(y_pos)
    plt.bar(y_pos, degeneracies)
    plt.xticks(y_pos, macrostates, fontsize=7, rotation=30)
    plt.legend(['System size: %i' % i], loc='upper right')
    plt.savefig('./Øvning 4/plots/density_of_states' + str(i))
    plt.clf()
    #Calculates the variance of the microstate list. The variance decreases as system size increases
    normalization_factor = max(m_AB) # The interaction energies are normalized
    normalized_mAB = [round(norm/normalization_factor, 2) for norm in m_AB] #Performs normalization
    print('%i particles:\nVariance: %6.4f\n' % (i, np.var(normalized_mAB))) #Prints variance

with open('./Øvning 4/pickle_files/m_AB.pkl', 'wb') as f: #Save microstate list along with system size for i = i_max (24 in this case)
    pickle.dump([m_AB,i], f)
