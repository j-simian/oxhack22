import math
import json

class Beatmap:
    def __init__(self, file=None):
        self.len = 0
        self.times = []
        self.angles = []
        self.angles_abs = []
        self.pos = []
        
        if file is not None:
            mapjson = json.loads(open(file, "r").read())
            mapbpm=float(mapjson["bpm"])
            self.bpm = mapbpm
            offset=float(mapjson["offset"])
            self.offset = offset
            beatTimes=[]
            beatAngles=[]
            for each in mapjson["beats"]:
                beatFraction=each[0]
                if len(beatFraction)==1:
                    time = offset+(60/mapbpm)*int(beatFraction[0])
                else:
                    time = offset+(60/mapbpm)*(int(beatFraction[0])+int(beatFraction[1])/int(beatFraction[2]))
                angle = each[1]
                self.add(time, angle, False)

    def add(self, time, angle, abs):
        self.len += 1

        prev_abs_angle = self.angles_abs[-1] if self.angles_abs else 0

        dt = time - self.times[-1] if self.times else time
        dx = dt * math.cos(prev_abs_angle * math.pi / 180)
        dy = dt * math.sin(prev_abs_angle * math.pi / 180)
        if self.pos:
            self.pos.append((self.pos[-1][0] + dx, self.pos[-1][1] + dy))
        else:
            self.pos.append((dx, dy))
        self.times.append(time)

        if abs:
            self.angles.append((angle - prev_abs_angle) % 360)
            self.angles_abs.append(angle)
        else:
            self.angles.append(angle)
            self.angles_abs.append((prev_abs_angle + angle) % 360)
