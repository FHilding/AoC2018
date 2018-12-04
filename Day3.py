import os, re
import numpy as np

myfile = open(os.path.join(os.path.dirname(__file__),'data/day3data.txt'), 'r')
contents = myfile.read().split("\n")
myfile.close()

def parse_line(line):
    id, _, offset, size = line.split(" ")
    x0, y0 = map(int, offset[:-1].split(",")) #Trim the :
    width, height = map(int, size.split("x"))
    return id, x0, y0, width, height

def part1(data):
    rect = np.zeros((1000,1000), dtype=np.int)
    for claim in data:
         _, x0, y0, width, height = parse_line(claim)
         rect[x0:x0+width, y0:y0+height] += 1
    return np.size(np.where(rect >= 2)[0])
    #return np.size(np.where(rect >= 2)[1])


def part2(data):
    rect = np.zeros((1000,1000), dtype=np.int)
    for claim in data:
        id, x0, y0, width, height = parse_line(claim)
        rect[x0:x0+width, y0:y0+height] += 1
    for claim in data:
        id, x0, y0, width, height = parse_line(claim)
        if np.all(rect[x0:x0+width, y0:y0+height] == 1):
            return id
    


print(part1(contents))
print(part2(contents))

