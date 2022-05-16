import numpy as np
import os

cwd = os.getcwd()

def pbc_r(v, d):
    for i in range(3):
        if v[i] > d[i] / 2:
            v[i] -= d[i]
        elif v[i] < -d[i] / 2:
            v[i] += d[i]

    return np.linalg.norm(v)

def harmlin(r, u0, r_cut):
    if r < r_cut:
        return (-u0/r_cut)*r + u0
    else:
        return 0

if 'testout.rst' in os.listdir(cwd):
    with open(cwd + '/testout.rst', 'r') as f:
        crds = np.genfromtxt(f, skip_header=5, max_rows=4800)
    with open(cwd + '/harmpairs.dat', 'r') as f:
        harmpairs = np.genfromtxt(f, skip_header=1)
    with open(cwd + '/crys.crds', 'r') as f:
        d = np.genfromtxt(f,
                          skip_header=(5 + 4800 + 3))
    with open(cwd + 'harm_au.inpt', 'r') as f:
        harm_au = np.genfromtxt(f, skip_header=8)
    u0 = float(harm_au[0, 0][:-2])
    r_cut = float(harm_au[1, 0][:, -2])
    E_harm = 0
    r_mx = 3.0387
    r_xx = 4.9624
    for i in range(harmpairs.shape[0]):
        atom1, atom2 = int(harmpairs[i, 0]), int(harmpairs[i, 1])
        if atom1 > 3200 or atom2 > 3200:
            r0 = r_mx

        else:
            r0 = r_xx
        v = np.subtract(crds[atom1 - 1, :], crds[atom2 - 1, :])
        r = pbc_r(v, d)
        E_harm += 0.5 * 1.001 * (r - r0) ** 2
    ## xx
    E_xx = 0
    for atom1 in range(3199):
        for atom2 in range(atom1 + 1, 3200):
            v = np.subtract(crds[atom1, :], crds[atom2, :])
            r = pbc_r(v, d)
            E_xx += harmlin(r, u0, r_cut)

    ## mm
    E_mm = 0
    for atom1 in range(3200, 4799):
        for atom2 in range(atom1 + 1, 4800):
            v = np.subtract(crds[atom1, :], crds[atom2, :])
            r = pbc_r(v, d)
            E_mm += harmlin(r, u0, r_cut)

