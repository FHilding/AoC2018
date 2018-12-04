from collections import Counter, OrderedDict
import os
myfile = open(os.path.join(os.path.dirname(__file__),'data/day2data.txt'), 'r')
contents = myfile.read().strip().split()
contents2 = contents.copy()
myfile.close()

twos = 0
threes = 0
for line in contents:
    cnt = Counter(line)
    cnt.subtract(list(set(line)))
    filteredValues = [x for x in cnt.values() if int(x)>0]
    if 1 in filteredValues:
        twos+=1
    if 2 in filteredValues:
        threes+=1

print(twos*threes)


for line in contents:
    for line2 in contents2:
        if line != line2:
            zipped = zip(line, line2)
            differs = [x for x in zipped if x[0]!=x[1]]
            if len(differs)==1:
                same = ''.join([x[0] for x in zip(line, line2) if x[0]==x[1]])
                print(same)
                break
    contents2.pop(0)
    
