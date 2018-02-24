import io
import os
import sys
import numpy as np


name = sys.argv[1]
file=open(name,"r")
lines = file.readlines()
file.close()


ef_line = lines[6].split()
ef = float(ef_line[3])

print ef," 0"

emax = ef + 1.5
emin = ef - 1.5

for i in range(15,len(lines)):
    line = lines[i].split()
    if len(line)==2:
        k = float(line[0])
        e = float(line[1])
        if e < emax:
            if e > emin:
                print k,e
