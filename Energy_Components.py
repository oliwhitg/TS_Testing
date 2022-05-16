import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors

static_steps = 100000
harmonic_steps = 1000000
count = 0
statics = []
harmonics = []
with open("{:}_data_export.dat".format(static_steps), 'r') as f:
    while True:
        line = f.readline()
        # if line is empty
        # end of file is reached
        if not line:
            break
        if 'static_{:}'.format(static_steps) in line.strip().split():
            statics.append(count)
        count += 1

with open("{:}_data_export.dat".format(static_steps), 'r') as f:
    static_array = np.genfromtxt(f)
count =0
with open("{:}_data_export.dat".format(harmonic_steps), 'r') as f:
    while True:
        line = f.readline()
        # if line is empty
        # end of file is reached
        if not line:
            break
        if 'static_{:}'.format(harmonic_steps) not in line.strip().split():
            harmonics.append(count)
        count += 1

with open("{:}_data_export.dat".format(harmonic_steps), 'r') as f:
    harmonic_array = np.genfromtxt(f)

viridis = cm.get_cmap('viridis')
cmap = plt.get_cmap("viridis")

# 567                      -1732                    0                        harmonic_100000          10                       700                      0.0203118399

static_ring_limits  = static_array[:, 0]
static_t_list       = static_array[:, 1]
static_i_list       = static_array[:, 4]
static_a_list       = static_array[:, 5]
static_e_list       = static_array[:, 6]
static_pe_list      = static_array[:, 7]
static_ke_list      = static_array[:, 8]
static_rim_list     = static_array[:, 9]

harmonic_ring_limits    = harmonic_array[:, 0]
harmonic_t_list         = harmonic_array[:, 1]
harmonic_i_list         = harmonic_array[:, 4]
harmonic_a_list         = harmonic_array[:, 5]
harmonic_e_list         = harmonic_array[:, 6]
harmonic_pe_list        = harmonic_array[:, 7]
harmonic_ke_list        = harmonic_array[:, 8]
harmonic_rim_list       = harmonic_array[:, 9]

dict_statics = {}
for i in statics:

    T = static_t_list[int(i)]
    if str(T) not in dict_statics.keys():
        dict_statics['{:}'.format(T)] = {}

    vals = static_i_list[int(i)]

    if str(vals) not in dict_statics['{:}'.format(T)].keys() and int(float(static_ring_limits[int(i)])) == 567:
        dict_statics['{:}'.format(T)]['{:}'.format(vals)] = {}
        dict_statics['{:}'.format(T)]['{:}'.format(vals)]['Area'] = []
        dict_statics['{:}'.format(T)]['{:}'.format(vals)]['Energy'] = []
        dict_statics['{:}'.format(T)]['{:}'.format(vals)]['PE'] = []
        dict_statics['{:}'.format(T)]['{:}'.format(vals)]['KE'] = []
        dict_statics['{:}'.format(T)]['{:}'.format(vals)]['RIM'] = []

    if int(float(static_ring_limits[int(i)])) == 567:
        dict_statics['{:}'.format(T)]['{:}'.format(vals)]['Area'].append(static_a_list[i])
        #        dict_statics['{:}'.format(T)]['{:}'.format(vals)]['Energy'].append(np.log10(e_list[i]))
        dict_statics['{:}'.format(T)]['{:}'.format(vals)]['Energy'].append(static_e_list[i])
        dict_statics['{:}'.format(T)]['{:}'.format(vals)]['PE'].append(static_pe_list[i])
        dict_statics['{:}'.format(T)]['{:}'.format(vals)]['KE'].append(static_ke_list[i])
        dict_statics['{:}'.format(T)]['{:}'.format(vals)]['RIM'].append(static_rim_list[i])

dict_harmoinics = {}
for i in harmonics:

    T = harmonic_t_list[int(i)]
    if str(T) not in dict_harmoinics.keys():
        dict_harmoinics['{:}'.format(T)] = {}

    vals = harmonic_i_list[int(i)]

    if str(vals) not in dict_harmoinics['{:}'.format(T)].keys() and int(float(harmonic_ring_limits[int(i)])) == 567:
        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)] = {}
        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)]['Area'] = []
        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)]['Energy'] = []
        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)]['PE'] = []
        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)]['KE'] = []
        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)]['RIM'] = []

    if int(float(harmonic_ring_limits[int(i)])) == 567:
        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)]['Area'].append(harmonic_a_list[i])
        #        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)]['Energy'].append(np.log10(e_list[i]))
        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)]['Energy'].append(harmonic_e_list[i])
        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)]['PE'].append(harmonic_pe_list[i])
        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)]['KE'].append(harmonic_ke_list[i])
        dict_harmoinics['{:}'.format(T)]['{:}'.format(vals)]['RIM'].append(harmonic_rim_list[i])



print(dict_harmoinics)

norm_angle = matplotlib.colors.Normalize(vmin=0, vmax=110)

print('\nT')
print(dict_statics.keys())
print(dict_harmoinics.keys())

fig, ax1 = plt.subplots()
ax1.set_xlabel('Area')
ax1.set_ylabel('ts_rim Energy', color='k')
ax1.tick_params(axis='y', labelcolor='k')
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('Width of Bilayer', color='b')  # we already handled the x-label with ax1
ax2.tick_params(axis='y', labelcolor='b')

for T in dict_statics.keys():
    if T in dict_harmoinics.keys():


        intercepts = sorted(dict_statics['{:}'.format(T)].keys())
        print('\nIntercepts')
        print(sorted(dict_statics['{:}'.format(T)].keys()))
        print(sorted(dict_harmoinics['{:}'.format(T)].keys()))

        list_intercepts = [float(intercept) for intercept in intercepts]
        list_intercepts = sorted(list_intercepts)
        for intercept in list_intercepts:
            if '{:}'.format(intercept) in dict_harmoinics['{:}'.format(T)].keys() and int(intercept)>65:

                print('Intercept : ', intercept)
                x       = dict_statics['{:}'.format(T)]['{:}'.format(intercept)]['Area']
                yse     = dict_statics['{:}'.format(T)]['{:}'.format(intercept)]['Energy']
                yspe    = dict_statics['{:}'.format(T)]['{:}'.format(intercept)]['PE']
                yske    = dict_statics['{:}'.format(T)]['{:}'.format(intercept)]['KE']
                ysrim   = dict_statics['{:}'.format(T)]['{:}'.format(intercept)]['RIM']

                yhe     = dict_harmoinics['{:}'.format(T)]['{:}'.format(intercept)]['Energy']
                yhpe    = dict_harmoinics['{:}'.format(T)]['{:}'.format(intercept)]['PE']
                yhke    = dict_harmoinics['{:}'.format(T)]['{:}'.format(intercept)]['KE']
                yhrim   = dict_harmoinics['{:}'.format(T)]['{:}'.format(intercept)]['RIM']

#                y11 = [i + 0 * float(intercept) for i in y11]

                x, yse, yspe, yske, ysrim, yhe, yhpe, yhke, yhrim = zip(*sorted(zip(x, yse, yspe, yske, ysrim, yhe, yhpe, yhke, yhrim)))

#                ax1.plot([x[i] / 1000 for i in range(len(x))], yse, '-', color='r',     alpha=0.4,
#                         label='Engtot Static')
                ax1.plot([x[i] / 1000 for i in range(len(x))], [int(intercept/100) + np.log10(i-min(yspe)+10**-10) for i in yspe], '-', color=viridis(norm_angle(float(intercept))),    alpha=0.4,
                         label='PE_Static {:}'.format(intercept))
#                ax1.plot([x[i] / 1000 for i in range(len(x))], yske, '-', color='g',   alpha=0.2,
#                         label='KE_Static')
#                ax1.plot([x[i] / 1000 for i in range(len(x))], ysrim, '-', color='y',   alpha=0.4,
#                         label='RIM_Static')

#                ax2.plot([x[i] / 1000 for i in range(len(x))], [(i) for i in yhe], '--', color='r',     alpha=0.4,
#                         label='Engtot Harmonic')
#                ax2.plot([x[i] / 1000 for i in range(len(x))], [np.log10(i-min(yhpe)+10**-10) for i in yhpe], '--', color=viridis(norm_angle(float(intercept))),    alpha=0.4,
#                         label='PE_Harmonic {:}'.format(intercept))
#                ax2.plot([x[i] / 1000 for i in range(len(x))], [np.log10(yhpe[i]) for i in yhpe], '--', color='b',
#                         label='PE_Harmonic')
#                ax2.plot([x[i] / 1000 for i in range(len(x))], [(i) for i in yhrim], '--', color='y',   alpha=0.4,
#                         label='RIM_Harmonic')



            #            ax2.plot([x[i]/1000 for i in range(len(x))], [2*4.9624*np.sqrt(2/3) for i in range(len(x))], color='k')
fig.legend()
#plt.xlim(0.9,1.1)
fig.suptitle('Temperature : {:}, Intercept : {:}'.format(T, intercept))
plt.show()

