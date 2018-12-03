myfile = open('data/day1data.txt', 'r')
contents = myfile.read().strip().split()
myfile.close()

print(sum([int(x) for x in contents]))
start = 0
matchedFrequencies = set([start])
matched = False
while matched != True:
    for line in contents:
        start += int(line)
        if start in matchedFrequencies:
            matched = True
            break
        else:
            matchedFrequencies.add(start)

print(start)
