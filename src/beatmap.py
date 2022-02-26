mapfile = open("res/map.txt","r")
maplines = []
for eachline in mapfile:
    maplines.append(str(eachline))

bpm=eachline[0]
offset=eachline[1]
beatTimes=[]
for eachline in maplines[2:]:
    beatTimes.append(float(eachline))

print(beatTimes)