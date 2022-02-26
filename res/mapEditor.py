import json
import math
from beatmap import Beatmap 


def main():
    beatmap = Beatmap("map.json")
    x = input()
    while(x != "q"):
        val = float(x)/8 + beatmap.times[len(beatmap.times)-1]
        angle = input()
        beatmap.times.append(val)
        beatmap.angles.append(int(angle))
        x = input()
    jsonmap = {}
    jsonmap["bpm"] = 120
    jsonmap["offset"] = 0
    jsonmap["beats"] = []
    for i in range(0, len(beatmap.angles)):
        beatmap.times[i] = [math.floor(beatmap.times[i]*2), int(((beatmap.times[i]*2)%1)*4), 4]
        jsonmap["beats"].append([beatmap.times[i], beatmap.angles[i]])
    print(jsonmap)
    upload = open("map.json", "w")
    upload.write(json.dumps(jsonmap))
    upload.close()

if __name__ == "__main__":
    main()
