mapfile = open("res/map.txt","r")
maplines = []
for eachline in mapfile:
    maplines.append(str(eachline))

mapbpm=float(maplines[0])
offset=float(maplines[1])
beatTimes=[]
for eachline in maplines[2:]:
    beatTimes.append(int(eachline))