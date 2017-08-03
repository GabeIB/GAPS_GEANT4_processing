#Gabriel Brown
#Summer 2017 GAPS Lab
#Creates histogram from multiplicity data stored in txt file


import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

#parameter to modify
particle = sys.argv[1] #type of particle.... either antiproton or antideuteron or comp
output = sys.argv[2] #type of output.... either multiplicity or xray-energy

def fileRead(particle, output):
	quants = list(csv.reader(open(particle+" "+output+".txt", 'r'),delimiter = '\n'))
	quants = [int(float(i[0])) for i in quants]
	quants = np.asarray(quants)
	return quants

def plotWrite(array, particle, output):
	kev_range = [20,80]
	plt.xlabel(output+' of each event')
	plt.ylabel('Number of events')
	plt.title('Histogram of '+output+' from '+particle+' Event')
	plt.grid(True)
	if(output=="multiplicity"):
		plt.axis([0,20,0,1])
		plt.hist(array, bins=range(0,20), normed=1)
	elif(output=="xray-energy"):
		plt.axis([kev_range[0],kev_range[1],0,1])
		plt.hist(array, bins=range(kev_range[0],kev_range[1]), normed=1)

if(particle == "comp"): #compare both particles
	pbar = fileRead("antiproton",output)
	dbar = fileRead("antideuteron",output)
	plt.subplot(211)
	plotWrite(pbar,"antiproton",output)
	plt.subplot(212)
	plotWrite(dbar,"antideuteron",output)

	left  = 0.125  # the left side of the subplots of the figure
	right = 0.3    # the right side of the subplots of the figure
	bottom = 0.1   # the bottom of the subplots of the figure
	top = 0.9      # the top of the subplots of the figure
	wspace = 0.3   # the amount of width reserved for blank space between subplots
	hspace = 0.4   # the amount of height reserved for white space between subplots
	plt.subplots_adjust(hspace=.7)
else:
	quants = fileRead(particle,output)
	average = np.mean(quants)
	standard_deviation = np.std(quants)
	print("average "+output+" of "+particle+" event = "+str(average))
	print("standard deviation of set of "+particle+" events = " + str(standard_deviation))
	plotWrite(quants,particle,output)



plt.show()
