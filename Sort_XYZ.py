import numpy as np
import os
import time

current_dir = os.getcwd()

def pbc_r(v, d):
    for i in range(3):
        if v[i] > d[i]/2:
            v[i] -= d[i]
        elif v[i] < -d[i]/2:
            v[i] += d[i]

    return np.linalg.norm(v)

intercept = 5

for minimisation_number in [10000, 100000,510000,600000]:

    if os.path.isfile(current_dir+"/{:}_{:}_vmd_export.dat".format(minimisation_number, intercept)) == True:
        with open('{:}_{:}_vmd_export.dat'.format(minimisation_number, intercept), 'r') as output:
    
            run_data = np.genfromtxt(output, dtype=str)
            print(run_data)
            time.sleep(1)
            previous_results = True
    else:
        previous_results = False
    
    
    
    
    with open('{:}_{:}_vmd_export.xyz'.format(minimisation_number, intercept), 'a+') as output:
    
        cwd = current_dir+"/Minimisations/567/T-1600/t-1600_s0_same/static/static_{:}/intercept_{:}".format(minimisation_number, intercept)

        for areas in os.listdir(cwd):
    
            print('    ', '    ', '    ',
                  '    ', '    ', areas)
    
            if os.path.isdir(current_dir+"/Minimisations/567/T-1600/t-1600_s0_same/static/static_{:}/intercept_{:}".format(minimisation_number, intercept) +"/" + areas):
                cwd = current_dir + "/Minimisations/567/T-1600/t-1600_s0_same/static/static_{:}/intercept_{:}".format(minimisation_number, intercept) + "/" + areas

                area = int(areas[5:])
                if previous_results == False:
                     print('No previous Results')

                    if 'testout.rst' in os.listdir(cwd):
                        with open(cwd + '/testout.rst', 'r') as f:
                            crds = np.genfromtxt(f, skip_header=5, max_rows=4800)
                        with open(cwd + '/crys.crds', 'r') as f:
                            dims = np.genfromtxt(f, skip_header=(5+4800+3))

                        output.write('4800\n{:}\n'.format(area))
                        for i in range(3200):
                            output.write('O{:<11}{:<30}{:<30}{:<30}\n'.format(i, crds[i,0], crds[i,1], crds[i,2]))
                        for i in range(3200,4800):
                            output.write('Si{:<10}{:<30}{:<30}{:<30}\n'.format(i-3200, crds[i,0], crds[i,1], crds[i,2]))


                        print('++')
                    else:
                        print('--')
    
#                else:
#                     print('Found old run_data and using it')
#                    to_write = [
#                        str(int(rings)), str(T), str(seed), str(protocol+'_{:}'.format(minimisation_number)), str(I), str(area)]
#                    new_bool = True
#                     print(run_data)
#                    for i in range(run_data.shape[0]):
#                         print(run_data[i,:], to_write)
#                        if to_write[0]==run_data[i,0] and to_write[1]==run_data[i,1] and to_write[2]==run_data[i,2] and to_write[2]==run_data[i,2] and to_write[3]==run_data[i,3] and to_write[4]==run_data[i,4] and to_write[5]==run_data[i,5]:
#
#                            new_bool = False
#                            print('==')
#
#                    if new_bool == True:
#                            if 'engtot.out' in os.listdir(cwd):
#                                with open(cwd+'/engtot.out', 'r') as f:
#                                    array = np.genfromtxt(
#                                        f)
#                                E = array[-1, 2]
#                                output.write('{:<25}{:<25}{:<25}{:<25}{:<25}{:<25}'.format(
#                                    int(rings), T, seed, protocol+'_{:}'.format(minimisation_number), I, area))
#                                output.write(
#                                    '{:<10}\n'.format(E))
#                                print('++')
#                            else:
#                                print('--')
