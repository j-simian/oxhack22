import json

def load_beatmap():
    mapjson = json.loads(open("res/map.json","r").read())
    print(mapjson)
    mapbpm=float(mapjson["bpm"])
    offset=float(mapjson["offset"])
    beatTimes=[]
    beatAngles=[]
    for each in mapjson["beats"]:
        beatFraction=each[0]
        if len(beatFraction)==1:
            beatTimes.append(offset+(60/mapbpm)*int(beatFraction[0]))
        else:
            beatTimes.append(offset+(60/mapbpm)*(int(beatFraction[0])+int(beatFraction[1])/int(beatFraction[2])))
        beatAngles.append(each[1])
    return(beatTimes,beatAngles,mapbpm,offset)