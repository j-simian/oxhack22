import json

class Beatmap:
    def __init__(self, file):
        mapjson = json.loads(open(file, "r").read())
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

        self.len = len(beatTimes)
        assert len(beatTimes) == len(beatAngles)
        self.times = beatTimes
        self.angles = beatAngles
        self.bpm = mapbpm
        self.offset = offset
