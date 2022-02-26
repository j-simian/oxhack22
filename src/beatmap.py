def load_beatmap():
    mapfile = open("res/map.txt","r")
    maplines = []
    for eachline in mapfile:
        maplines.append(str(eachline))

    mapbpm=float(maplines[0])
    offset=float(maplines[1])
    beatTimes=[]
    for eachline in maplines[2:]:
        beatFraction=eachline.split(',')
        if len(beatFraction)==1:
            beatTimes.append(offset+(60/mapbpm)*int(beatFraction[0]))
        else:
            beatTimes.append(offset+(60/mapbpm)*(int(beatFraction[0])+int(beatFraction[1])/int(beatFraction[2])))
    return(beatTimes)