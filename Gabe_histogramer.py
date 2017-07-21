import matplotlib.pyplot as plt
import numpy as np
import csv

#parameter to modify
read = 'antideuteron'

if(read == 'antiproton'):
	quants = list(csv.reader(open('pion quantities_pbar.txt', 'r'),delimiter = '\n'))
	quants = [int(float(i[0])) for i in quants]
	quants = np.asarray(quants)

	average = np.mean(quants)
	standard_deviation = np.std(quants)
	print("average multiplicity of antiproton event = " + str(average))
	print("standard deviation of set of antiproton events = " + str(standard_deviation))


	plt.hist(quants, bins=range(0,20))

	plt.xlabel('Pions produced per event')
	plt.ylabel('Number of events')
	plt.title('Histogram of Pion Multiplicity from Antiproton Event')
	plt.axis([0,20,0,4000])
	plt.grid(True)
	plt.show()

if(read =='antideuteron'):
	quants = list(csv.reader(open('pion quantities_dbar.txt', 'r'),delimiter = '\n'))
	quants = [int(float(i[0])) for i in quants]
	quants = np.asarray(quants)

	average = np.mean(quants)
	standard_deviation = np.std(quants)
	print("average multiplicity of antideuteron event = " + str(average))
	print("standard deviation of set of antideuteron events = " + str(standard_deviation))

	plt.hist(quants, bins=range(0,20))

	plt.xlabel('Pions produced per event')
	plt.ylabel('Number of events')
	plt.title('Histogram of Pion Multiplicity from Antideuteron Event')
	plt.axis([0,20,0,4000])
	plt.grid(True)
	plt.show()