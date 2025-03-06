from numpy import zeros
from random import choice, uniform
import matplotlib.pyplot as plt
from math import log, factorial

row = 100               # row and col are the dimension of the lattice
col = 200
n = 50                # number of particles
num_steps = 10000             # number of simulation steps
dump_interval = num_steps/10     # should be around 1/10 of num_steps, a bad choice (too frequent) can make the calculation very slow 

def initialize(row, col, n):
    """
    Put all the particles on for example the left-hand side
    """
    positions_of_particles = []
    for i in range(n):
        positions_of_particles.append((i%row, i//row))
    print(positions_of_particles)
    return positions_of_particles

def possible_transitions(positions_of_particles):
    """
    Calculate the possible transitions from the positions
    """
    transitions = []
    for particle_inc, pos in enumerate(positions_of_particles):
        for incr in [(1,0),(0,-1),(-1,0),(0,1)]:
            new_pos = (pos[0] + incr[0], pos[1] + incr[1])
            if new_pos not in positions_of_particles and 0 <= new_pos[0] < row and 0 <= new_pos[1] < col:
                transitions.append((particle_inc, new_pos))
    return transitions

def perform_transition(positions_of_particles, transitions):
    """
    Choose a random transition and update the positions
    """
    Choosen_transition = choice(transitions)
    positions_of_particles[Choosen_transition[0]] = Choosen_transition[1]
    return positions_of_particles

def entropy_calc(positions_of_particles, n):
    """
    Use the min and max functions to obtain "lattice_spread" 
    """
    lattice_spread = (max([pos[0] for pos in positions_of_particles]) - min([pos[0] for pos in positions_of_particles]) + 1) * (max([pos[1] for pos in positions_of_particles]) - min([pos[1] for pos in positions_of_particles]) + 1)
    return log(factorial(lattice_spread)/(factorial(n)*factorial(lattice_spread - n)))

def create_image(positions_of_particles, tr_num): 
    """
    tr_num is the actual simulation step  
    """
    #Create an array with a lattice and the occupied lattice points in positions_of_particles 
    current_state = zeros((row, col))
    for pos in positions_of_particles:
        current_state[pos] = 1
    imgplot = plt.imshow(current_state, cmap='binary')
    plt.savefig('./Øvning5/plots/lattice' + str(tr_num) + '.png')

#Main code starts
#Use the initialize function to create a list of all the particles positions
#Set up the list with possible transitions
#Set up lists for the time stamp and the local entropy that can be updated inside the loop

#Start the loop. Both a for-loop and a while-loop will work.
    #Update the positions lists using perform_transition()
    #Calculate the present time: time += "KMC equation for time". Note that the time is updated in every step but only stored when the entropy is stored
    #Recalculate the possible transitions (too complex to update, just recalculate from scratch
    #Remember to store an image at a regular interval. Use for example: if tr_num % dump_interval == 0:
    #Update the entropy and time stamp lists, also at a regular interval. Make sure that the time step list reflects the total time passed at any given point.
    #If using a while-loop, update tr_num

#The code below creates the plots the local entropy as a function of time.
positions_of_particles = initialize(row, col, n)
create_image(positions_of_particles, 0)

transitions = possible_transitions(positions_of_particles)
time = 0
local_entropy = []
time_step = []
for tr_num in range(num_steps):
    transitions = possible_transitions(positions_of_particles)
    positions_of_particles = perform_transition(positions_of_particles, transitions)
    time += -log(uniform(0,1))/len(transitions)
    if tr_num % dump_interval == 0:
        create_image(positions_of_particles, tr_num)
        local_entropy.append(entropy_calc(positions_of_particles, n))
        time_step.append(time)




plt.clf()
plt.plot(time_step, local_entropy)
plt.show()
