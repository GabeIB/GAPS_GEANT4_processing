import csv
import numpy as np

#parameter to modify
particle = 'antideuteron'

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
#list event_storage stores pions from event
event_storage = []
#make list perm_storage (this list stores lists) stores events
perm_storage = []

antiproton_track = -1
old_event = 0

antiproton_count = 0
antineutron_count = 0

def is_douplicate(new_id):
	is_it = -1
	ii=-1
	for element in event_storage:
		ii+=1
		old_id = element[1]
		if(old_id == new_id):
			is_it = ii
	return is_it

def is_first(new_time, douplicate_id):
	new_first = False
	old_time = float(event_storage[douplicate_id][7])
	if(new_time < old_time):
		new_first = True
	return new_first

def finalProcess(antiproton_track):
	global antiproton_count, antineutron_count
	antiproton_track += 1
	if(antiproton_track):
		antiproton_track -= 1
		antiproton_count += 1
		for pion in event_storage:
			local_parent_id = pion[2]
			if(local_parent_id != '1' and int(float(local_parent_id)) != antiproton_track):
				del(pion)
		perm_storage.append(event_storage)
	else:
		antineutron_count += 1
		#if it never saw an anti-proton, clear the whole list and do nothing
		 #clears the whole list
	
	#if it saw one, go through event_storage and delete all pions that didn't come from parent_id 1 or antiproton
	#append event_storage to perm_storage and clear event_storage

#~~~~~~~~~~main~~~~~~~~~~~~
for line in pfile:
	temp_storage = line.split('\t')
	event_id = int(float(temp_storage[0]))
	if(event_id != old_event):
		finalProcess(antiproton_track)
		old_event = event_id
		antiproton_track = -1
		event_storage = []
#check if element #3 is a pion id (-211, 211, 111) if(false) do nothing
	particle_id = temp_storage[3]
	track_id = temp_storage[1]
	#if an antiproton appears in event, set marker to true and note the track_id
	if(particle_id == '-2212'):
		antiproton_track = int(float(track_id))
	if(particle_id=='-211' or particle_id=='211' or particle_id=='111'):
#if(true) check if new_id (element #1) is the same as any particle_id's in perm_storage
#if(false) add temp_arry to perm storage
		new_id = temp_storage[1]
		#python reads any int != 0 as true and 0 as false
		#is_douplicate returns the index of a particle with matching id of new_id, and -1 if no matching id found
		#adding 1 in the if statement makes -1 into 0 so it reads as a boolean "false"
		#ask Gabe if it doesn't make sense
		douplicate_spot = is_douplicate(new_id)+1
		if(douplicate_spot): #returns true if there is already a particle with the same id
			douplicate_spot -= 1
			new_time = float(temp_storage[7])
			if(is_first(new_time, douplicate_spot)): #returns true if the new particle came before the old one with the same id
				#replace old particle with new particle
				del event_storage[douplicate_spot]
				event_storage.append(temp_storage)
		else:
			#add particle to perm_storage
			event_storage.append(temp_storage)
#final processing on event
#delete any pions where the parent_id isn't either 1 or the antiproton's id

	



#after this runs on the whole file, this should get a list of lists, each list containing a unique pion line

#making a multiplicity histogram from this

#make an int array with 10,000 slots call it "multiplicity"
multiplicity = np.zeros(len(perm_storage))
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

print("antineutron count = " + str(antineutron_count))
print("antiproton count = " + str(antiproton_count))


#this gives a list with multiplicity of each event
#ex: multiplicity[4] = number of pions in event 4
#turn this into a histogram with numpy? should be easy
