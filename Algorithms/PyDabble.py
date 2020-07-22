from array import *

vals = array('i', [2, 4, 6, 7])
vals.reverse()

for i in range(len(vals)):
    print(vals[i])

for a in vals:
    print(a)

newa = array(vals.typecode, (a * a for a in vals))

i = 0

while i < len(newa):
    print(newa[i])
    i += 1
