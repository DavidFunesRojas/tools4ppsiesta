# python maxforce.py output.txt
# It finds the maximun force (from the last structual relaxation step) from the output file
# 

import os
import sys
import io

filename = sys.argv[1]

infile = open(filename,"r")
lines = infile.readlines()
infile.close()  

nl = len(lines)

force = []


startforcemarker = "siesta: Atomic forces (eV/Ang):"
endforcemarker = "siesta: ----------------------------------------"

for k in range(0,nl-1):
	i = nl-1-k
	line = lines[i]

	if line[0:len(startforcemarker)]==startforcemarker :
		j = 1 

		while line[0:len(endforcemarker)]!=endforcemarker :
			line = lines[i+j]
			force.append(line[len("0000000    000    00000000 "):-1])
			j = j + 1
            
		if line[0:len(endforcemarker)]==endforcemarker :
			break
		
f = []

for i in range(0,len(force)-1):
	fi = force[i].split()
	fiy = abs(float(fi[0]))
	fiz = abs(float(fi[1]))	
	fimax = max([fiy,fiz])
	f.append(fimax)

print max(f)
