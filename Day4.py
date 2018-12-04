import os
from collections import defaultdict
myfile = open(os.path.join(os.path.dirname(__file__),'data/day4data.txt'), 'r')
contents = myfile.read().split("\n")
myfile.close()

guard_dict = defaultdict(lambda:[0 for x in range(60)])

for line in sorted(contents):
    time_portion, action_portion = line.split("] ")
    #date, time = separated[0].split(" ")
    if action_portion[0]=="G":
        guard_id = action_portion.split("#")[1].split(" ")[0]
    elif action_portion[0]=="f":
        minute_asleep = int(time_portion[-2:])
    else:
        minute_awake = int(time_portion[-2:])
        for minute in range(minute_asleep, minute_awake):
            guard_dict[guard_id][minute] +=1

    

  
max_sleep_guard_id = sorted([(sum(guard_dict[x]), x) for x in guard_dict.keys()], key=lambda x:x[0], reverse=True)[0][1]
print(guard_dict[max_sleep_guard_id].index(max(guard_dict[max_sleep_guard_id])), max_sleep_guard_id)

#part2
max_sleep_guard_id = sorted([(max(guard_dict[x]), x) for x in guard_dict.keys()], key=lambda x:x[0], reverse=True)
print(max_sleep_guard_id)
