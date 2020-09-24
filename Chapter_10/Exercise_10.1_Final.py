fhand = open('mbox-short.txt')
times=dict()
timeslist = []

for line in fhand:
    if not line.startswith('From'): continue
    line = line.split()
    time=line[1]
    times[time] = times.get(time, 0) + 1
    for time, count in times.items():
        timeslist.append((count, time))
        timeslist.sort(reverse=True)
for count, time in timeslist[:1]:
    print (time, count)
