import csv
import numpy as np

#parameter to modify
particle = 'antiproton'

if(particle == 'antiproton'):
	pfile = open('annihilation_pbar.dat', 'r')
	pfile = pfile.readlines()

	big_data = open("Gabes_output/list of pions_pbar.txt","w")
	histogram = open("Gabes_output/pion quantities_pbar.txt","w")
	print("running parse for antiproton")
elif(particle=='antideuteron'):
	pfile = open('annihilation_dbar.dat', 'r')
	pfile = pfile.readlines()

	big_data = open("Gabes_output/list of pions_dbar.txt","w")
	histogram = open("Gabes_output/pion quantities_dbar.txt","w")
	print("running parse for antideuteron")
else:
	print("particle not recognized")


#main


#make list temp_storage (this list stores strings)
temp_storage = []
#make list perm_storage (this list stores lists)
perm_storage = [[] for x in xrange(10000)]

def is_douplicate(new_id, event_id):
	is_it = -1
	ii=-1
	for element in perm_storage[event_id]:
		ii+=1
		old_id = element[1]
		if(old_id == new_id):
			is_it = ii
	return is_it

def is_first(new_time, event_id, douplicate_id):
	new_first = False
	old_time = perm_storage[event_id][douplicate_id][7]
	if(new_time < old_time):
		new_first = True
	return new_first

old_event = 0
#add first 19 elements from pfile to array temp_storage
for line in pfile:
	temp_storage = line.split('\t')
	parent_id = temp_storage[2]
#check if element #3 is a pion id (-211, 211, 111) if(false) do nothing
	if(parent_id=='1'):
		particle_id = temp_storage[3]
		if(particle_id=='-211' or particle_id=='211' or particle_id=='111'):
	#if(true) check if new_id (element #1) is the same as any particle_id's in perm_storage
	#if(false) add temp_arry to perm storage
			event_id = int(float(temp_storage[0]))
			if(event_id != old_event and int(event_id)%100==0):
				old_event = event_id
				print("event " + str(event_id))
			new_id = temp_storage[1]
			new_time = temp_storage[7]
			#python reads any int != 0 as true and 0 as false
			#is_douplicate returns the index of a particle with matching id of new_id, and -1 if no matching id found
			#adding 1 in the if statement makes -1 into 0 so it reads as a boolean "false"
			#ask Gabe if it doesn't make sense
			douplicate_id = is_douplicate(new_id, event_id)+1
			if(douplicate_id): #returns true if there is already a particle with the same id
				douplicate_id -= 1
				if(is_first(new_time, event_id, douplicate_id)): #returns true if the new particle came before the old one with the same id
					#replace old particle with new particle
					del perm_storage[event_id][douplicate_id]
					perm_storage[event_id].append(temp_storage)
			else:
				#add particle to perm_storage
				perm_storage[event_id].append(temp_storage)



#after this runs on the whole file, this should get a list of lists, each list containing a unique pion line

#making a multiplicity histogram from this

#make an int array with 10,000 slots call it "multiplicity"
multiplicity = np.zeros(10000)
#for every list within perm storage, check the event_id (element #0)
ii=0
for event in perm_storage:
	event_multiplicity = len(event)
#convert to an int (should be '0' or '1' and turn that into 0 or 1)
#add 1 to multiplicity[x] where x is the event_id
	multiplicity[ii]=event_multiplicity
	ii+=1

for events in perm_storage:
	for pions in events:
		big_data.write(str(pions)+'\n')

for values in multiplicity:
	histogram.write(str(values)+'\n')


#this gives a list with multiplicity of each event
#ex: multiplicity[4] = number of pions in event 4
#turn this into a histogram with numpy? should be easy
