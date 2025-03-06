from random import uniform #will be used to pick random numbers between 0 and 1
from math import log
import matplotlib.pyplot as plt #Will be used to create the relevant plots
import numpy as np

#Part 1
n_a = 300#Number of particles of type A
n_b = 200#Number of particles of type B
n_c = 0#Number of particles of type C

k_f = 5#Kinetic forward constant
k_r = 1#Kinetic reverse constant

def probability_forward(k_f, k_r, n_a, n_b, n_c): 
    """
    Calculates the probability of a forward transition. The reverse probability is 1 - forward.
    """
    p_f = k_f*n_a*n_b/(k_f*n_a*n_b + k_r*n_c)
    return p_f#Use equation 5 in the exercise file

#Part 2
max_num_trans = 10000
num_trans = 0  #Sets up transition counter
equilibrium = False #Sets up equilibrium check
n_a_time = np.zeros(max_num_trans) #Inititates a list with number of A particles at each time step; for plotting
n_a_time[0] = n_a
n_b_time = np.zeros(max_num_trans)#Inititates a list with number of B particles at each time step; for plotting
n_b_time[0] = n_b
n_c_time = np.zeros(max_num_trans)#Inititates a list with number of C particles at each time step; for plotting
n_c_time[0] = n_c
time = 0
time_step = np.zeros(max_num_trans)#Sets up a list with the time passed after each transition; for plotting
time_step[0] = 0
while not equilibrium and num_trans < max_num_trans-1:
    #Use uniform(0,1) (generates random number) to select either forward or reverse reaction
    p_f = probability_forward(k_f, k_r, n_a, n_b, n_c)
    p = uniform(0,1)
    if p < p_f:
        n_a -= 1
        n_b -= 1
        n_c += 1
    else:
        n_a += 1
        n_b += 1
        n_c -= -1
    num_trans += 1
    n_a_time[num_trans] = n_a
    n_b_time[num_trans] = n_b
    n_c_time[num_trans] = n_c
    time += -log(p)/(k_f*n_a*n_b + k_r*n_c)
    time_step[num_trans] = time

    if p_f < 0.500:
        equilibrium = True
        print("Equilibrium reached")

    #Use incr = ... int(uniform(0,1)) ... to get an increment as +1 or -1 for updating the number of A, B and C particles
    #Update the number of particles for A, B and C
    #Update the lists for plotting.
    #Check the equilibrium condition to see if it has been reached

#Part 3
#Show plot of number of each particle as a function of time. plt.plot(x-axis, y-axis, color)
print(num_trans)
n_a_time = n_a_time[:num_trans]
n_b_time = n_b_time[:num_trans]
n_c_time = n_c_time[:num_trans]
time_step = time_step[:num_trans]
print("Equilibrium constant: ")
print("When equilibrium reached: ", n_c_time[-1]/(n_a_time[-1]*n_b_time[-1]), " vs ","Estimated from k_f and k_r: ", k_f/k_r) 

plt.plot(time_step, n_a_time, 'r', label='A')
plt.plot(time_step, n_b_time, 'b', label='B')
plt.plot(time_step, n_c_time, 'g', label='C')
plt.legend()
plt.show()

