# This one does not produce a fine of best fit
# Paste the data you wish to graph in tab-delimited rows in the format:
#
#       xdata <tab> ydata
#
# In this example the xdata is time (s) and y data is y position (cm)
#

print("This is a graph of y-position vs. time for a falling cupcake cup by Doug Brown and his students.")
print('http://www.cabrillo.edu/~dbrown/tracker/air_resistance.pdf')
print('')
print('Code is based on an example by Steve Spicklemire at:')
print('https://github.com/sspickle/sci-comp-notebooks/blob/master/P01-Euler-Intro.ipynb')

data = """
0.000000000E0	-2.688162330E0
3.336670003E-2	-4.301059729E0
6.673340007E-2	-5.376324661E0
1.001001001E-1	-6.989222059E0
1.334668001E-1	-1.129028179E1
1.668335002E-1	-1.451607658E1
2.002002002E-1	-2.043003371E1
2.335669002E-1	-2.526872591E1
2.669336003E-1	-3.118268303E1
3.003003003E-1	-3.870953756E1
3.336670003E-1	-4.623639208E1
3.670337004E-1	-5.430087907E1
4.004004004E-1	-6.236536606E1
4.337671004E-1	-7.150511799E1
4.671338005E-1	-8.010723744E1
5.005005005E-1	-8.924698937E1
5.338672005E-1	-9.892437376E1
5.672339006E-1	-1.080641257E2
6.006006006E-1	-1.177415101E2
6.339673006E-1	-1.274188945E2
6.673340007E-1	-1.370962788E2
7.007007007E-1	-1.467736632E2
7.340674007E-1	-1.575263126E2
7.674341008E-1	-1.672036969E2
8.008008008E-1	-1.768810813E2
8.341675008E-1	-1.865584657E2
8.675342009E-1	-1.973111150E2
9.009009009E-1	-2.075261319E2
9.342676009E-1	-2.182787812E2
9.676343010E-1	-2.284937981E2
""".split('\n')  # split this string on the "newline" character.

#print len(data)


#
# The data is stored in a single string. Now, split the data and store
# each column in a list. Convert the data from a string to a float.
#

tlist = []
ylist = []
for s in data:
    if s:
        t,y = s.split()     # split the string in two
        t=float(t)          # convert time to float
        y=float(y)/100.0    # convert y-position (cm) to float in meters
        tlist.append(t)     # append to the list for time data
        ylist.append(y)     # append to the list for y-position data
        
#print "tlist=",tlist
#print "ylist=",ylist

import matplotlib.pyplot as plt
plt.title('y-position vs. time for falling cupcake paper')
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.plot(tlist,ylist,'m.')
plt.show()
