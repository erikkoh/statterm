import numpy as np
from math import factorial, sqrt, exp, log
import matplotlib.pyplot as plt
import pickle

def calculate_F(m_AB):
    """
    Plots the Helmholtz free energy as a function of the energy for different temperatures.
    Given is a list of microstates, m_AB
    """
    macrostates = sorted(list(set(m_AB))) # Get macrosteps. Sorts list in ascending order
    # Obtain a list of degeneracies (same as in Task 1)
    degeneracies = [sum( 1 for i in m_AB if i == j) for j in macrostates] # ADD your code
    temperatures = np.linspace(1, 10, num=4) # the temperature range 
    for temp in temperatures:
        # Calculate a list with free energies. Use list comprehension. Hint: use zip(macrostates, degeneracies) as iterator
        free_energies = [U - temp*log(W) for U, W in zip(macrostates, degeneracies)] # ADD your code
        plt.plot(macrostates, free_energies)
        plt.legend(['T = %.2f' % temp for temp in temperatures], loc='best')
    plt.savefig('./Øvning 4/plots/helmholtz_free_energy') #Saves plot as Helmholtz_free_energy.png
    plt.close()

with open('./Øvning 4/pickle_files/m_AB.pkl', 'rb') as f: # Loads microstate list
    m_AB = pickle.load(f)[0]
calculate_F(m_AB)
