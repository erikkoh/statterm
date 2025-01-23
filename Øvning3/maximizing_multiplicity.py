from math import log
import matplotlib.pyplot as plt

def stirling(n):
    """
    Return ln n! using Stirling's approximation
    """
    return n*log(n) - n


def plot_multiplicity():
    lattice_points =10_000  # try with various numbers
    particles = [n for n in range(1,lattice_points)]# a list, number of particles use the range function: empty to completely filled lattice
    multiplicities_ln = [(stirling(lattice_points)-stirling(i)-stirling(lattice_points-i)) for i in particles] # use list comprehension to get list of ln W

    # plot ln W vs particles for a given number of lattice points
    # fill in the arguments to the functions below
    plt.plot(particles, multiplicities_ln, label='ln W')
    plt.title("Multiplicity as a function of particles")
    plt.ylabel("ln W")
    plt.xlabel("Particles")
    plt.show()

plot_multiplicity()
