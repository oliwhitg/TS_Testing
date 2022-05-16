import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors

steps = 100000
count = 0
statics = []
with open("{:}_data_export.dat".format(steps), 'r') as f:
    while True:
        line = f.readline()
        # if line is empty
        # end of file is reached
        if not line:
            break
        if 'static_{:}'.format(steps) in line.strip().split():
            statics.append(count)
        count +=1
print(statics)

with open("{:}_data_export.dat".format(steps), 'r') as f:
    array = np.genfromtxt(f)
print(array)
viridis = cm.get_cmap('viridis')
cmap = plt.get_cmap("viridis")


#567                      -1732                    0                        harmonic_100000          10                       700                      0.0203118399

ring_limits = array[:,0]
t_list = array[:,1]
i_list = array[:,4]
a_list = array[:,5]
e_list = array[:,6]
pe_list = array[:,7]
ke_list = array[:,8]
rim_list = array[:,9]
print(t_list)


dict = {}
for i in statics:

    T = t_list[int(i)]
    if str(T) not in dict.keys():
        dict['{:}'.format(T)] = {}

    vals = i_list[int(i)]

    if str(vals) not in dict['{:}'.format(T)].keys() and int(float(ring_limits[int(i)])) == 567:
        dict['{:}'.format(T)]['{:}'.format(vals)] = {}
        dict['{:}'.format(T)]['{:}'.format(vals)]['Area'] = []
        dict['{:}'.format(T)]['{:}'.format(vals)]['Energy'] = []

    if int(float(ring_limits[int(i)])) == 567:
        dict['{:}'.format(T)]['{:}'.format(vals)]['Area'].append(a_list[i])
#        dict['{:}'.format(T)]['{:}'.format(vals)]['Energy'].append(np.log10(e_list[i]))
        dict['{:}'.format(T)]['{:}'.format(vals)]['Energy'].append(e_list[i])
        dict['{:}'.format(T)]['{:}'.format(vals)]['PE'].append(e_list[i])
        dict['{:}'.format(T)]['{:}'.format(vals)]['KE'].append(e_list[i])
        dict['{:}'.format(T)]['{:}'.format(vals)]['RIM'].append(e_list[i])



print(dict)

norm_angle = matplotlib.colors.Normalize(vmin=0, vmax=110)
def max_lt(seq, val):
    return max([v for v in seq if v < val])
print(norm_angle(5.0))
dimz_list = []
filename = '100000_90_vmd_export_static.xyz'
with open(filename, 'r') as file:
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
#
#for i in range(int(line_count/4802)):
#    with open(filename, 'r') as f:
#        print('\n', i)
#        print(4802*i + 2)
#        temp_array = np.genfromtxt(f,skip_header=i*4802+2, max_rows=4800)
#        print(temp_array)
#        dimx = max(temp_array[:,1])-min(temp_array[:,1])
#        dimy = max(temp_array[:,2])-min(temp_array[:,2])
#        dimz = max_lt(temp_array[:,3],100)-min(temp_array[:,3])
#        print(dimx, dimy, dimz)
#        dimz_list.append(dimz)
#
for T in dict.keys():
    fig, ax1 = plt.subplots()


    intercepts = sorted(dict['{:}'.format(T)].keys())
    print(intercepts)
    list_intercepts = [float(intercept) for intercept in intercepts]
    list_intercepts = sorted(list_intercepts)
    print(intercepts)
    print(list_intercepts)
    for intercept in list_intercepts:


        if int(float(intercept))==90:
#        if 1>0:
            x = dict['{:}'.format(T)]['{:}'.format(intercept)]['Area']
            y = dict['{:}'.format(T)]['{:}'.format(intercept)]['Energy']
            y = [i + 0*float(intercept) for i in y]
            x, y = zip(*sorted(zip(x, y)))
            ax1.set_xlabel('Area')
            ax1.set_ylabel('ts_rim Energy', color='k')
            ax1.tick_params(axis='y', labelcolor='k')

            ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

            ax2.set_ylabel('Width of Bilayer', color='b')  # we already handled the x-label with ax1
#            ax2.plot([x[i]/1000 for i in range(len(x))], dimz_list, color='b')
            ax2.tick_params(axis='y', labelcolor='b')
            ax1.plot([x[i]/1000 for i in range(len(x))],y,color=viridis(norm_angle(float(intercept))), label='{:}'.format(int(float(intercept))))

            ax1.tick_params(axis='y', labelcolor=viridis(norm_angle(float(intercept))))

#            ax2.plot([x[i]/1000 for i in range(len(x))], [2*4.9624*np.sqrt(2/3) for i in range(len(x))], color='k')
    plt.legend()
    plt.title('Temperature : {:}  at {:} steps'.format(T, steps))
    #plt.ylim(0,250)
    plt.show()





    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()