import json



def main():
    map = json.loads("map.json")
    print(map["beats"])
    while(input() != "q"):
        map["beats"].append()

if __name__ == "__main__":
    main()
