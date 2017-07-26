import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

#parameter to modify
particle = sys.argv[1] #type of particle.... either antiproton or antideuteron
output = sys.argv[2] #type of output.... either multiplicity or xray-energy


if(particle == 'antiproton'):
	quants = list(csv.reader(open(particle+" "+output+".txt", 'r'),delimiter = '\n'))
elif(particle == 'antideuteron'):
	quants = list(csv.reader(open('pion quantities_dbar.txt', 'r'),delimiter = '\n'))
else:
	print("particle not recognized")

quants = [int(float(i[0])) for i in quants]
quants = np.asarray(quants)

average = np.mean(quants)
standard_deviation = np.std(quants)
print("average "+output+" of "+particle+" event = "+str(average))
print("standard deviation of set of "+particle+" events = " + str(standard_deviation))


plt.hist(quants, bins=range(0,20), normed=1)

plt.xlabel(output+' of each event')
plt.ylabel('Number of events')
plt.title('Histogram of '+output+' from '+particle+' Event')
plt.axis([0,20,0,1])
plt.grid(True)
plt.show()
