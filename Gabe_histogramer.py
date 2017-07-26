import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

#parameter to modify
read = sys.argv[1] #type of particle.... either antiproton or antideuteron

if(read == 'antiproton'):
	quants = list(csv.reader(open('pion quantities_pbar.txt', 'r'),delimiter = '\n'))
elif(read == 'antideuteron'):
	quants = list(csv.reader(open('pion quantities_dbar.txt', 'r'),delimiter = '\n'))
else:
	print("particle not recognized")

quants = [int(float(i[0])) for i in quants]
quants = np.asarray(quants)

average = np.mean(quants)
standard_deviation = np.std(quants)
print("average multiplicity of " + read + " event = " + str(average))
print("standard deviation of set of "+read+" events = " + str(standard_deviation))


plt.hist(quants, bins=range(0,20), normed=1)

plt.xlabel('Pions produced per event')
plt.ylabel('Number of events')
plt.title('Histogram of Pion Multiplicity from '+read+' Event')
plt.axis([0,20,0,1])
plt.grid(True)
plt.show()
