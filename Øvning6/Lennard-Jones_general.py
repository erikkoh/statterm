from sympy import diff, symbols, sqrt
import numpy as np


#***************YOUR INPUT HERE*************#

x, y, z, r = symbols('x y z r')

eps = 0.997 #kj/mol
sig = 3.4 #Å

v_cartasian = 4*eps*((sig/sqrt(x**2 + y**2 + z**2))**12-(sig/sqrt(x**2 + y**2 + z**2))**6)
vdiff = [-diff(v_cartasian, var) for var in [x,y,z]]

#**************END YOUR INPUT HERE***********#

#Here we input the coordinates of the atoms. You can have as many atoms as you want, 
#and change the coordinates to whatever you like
atoms = np.array([[0.,0.,0.], [0.,0.,1.], [0.,1.,0.], [1.,0.,0.], [1.,1.,0.], [1.,0.,1.], [0.,1.,1.], [1.,1.,1.], [0.5, 0.5, 0.5]])

file = open("./Øvning6/output.txt", "w") #We write the output to a textfile
file.write('    Atom 1    ' + '    Atom2   ' + '    Force(x-dir)   Force(y-dir)   Force(z-dir) ' + '\n')

for i in range(len(atoms)):
    for j in range(i):
        res = atoms[i] - atoms[j]
        Fxyz = [tv.subs([(x,res[0]), (y,res[1]),  (z,res[2])]) for tv in vdiff]
        print("Between", atoms[i], "and", atoms[j], "we have the forces", Fxyz)
        file.write(str(atoms[i]) + " " + str(atoms[j]))
        file.write( "%14.2f %14.2f %14.2f" % (Fxyz[0], Fxyz[1], Fxyz[2]) + '\n')
file.close()
