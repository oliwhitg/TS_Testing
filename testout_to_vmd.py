import numpy as np
n_o = 648
n_c = int(n_o/3)
n_na = int(2*n_c)

with open('testout.rst', 'r') as f:
    array = np.genfromtxt(f, skip_header=5, max_rows=1296)

with open('testout.xyz', 'w') as f:
    f.write('{:}\n\n'.format(1296))
    for i in range(n_o):
        f.write('O{:}    {:<20}{:<20}{:<20}\n'.format(int(i), array[i,0], array[i,1], array[i,2]))

    for i in range(n_o, n_o+n_c):
        f.write('C{:}    {:<20}{:<20}{:<20}\n'.format(int(i-n_o), array[i, 0], array[i, 1], array[i, 2]))

    for i in range(n_o+n_c, n_o+n_c+n_na):
        f.write('Na{:}    {:<20}{:<20}{:<20}\n'.format(int(i-n_o-n_c), array[i, 0], array[i, 1], array[i, 2]))

