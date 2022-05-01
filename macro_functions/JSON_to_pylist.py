import json
class JSONToPyList():
    def __init__(self):
        self = self
    def start():
        # Open existing JSON file!
        f = open("exported_JSON/JSON_new.json", "r")
        jsonStr = f.read()
        data = json.loads(jsonStr)
        name_list = data['items']
        print(len(name_list))
        for i in range (0, len(name_list)-1, 1):
            print(name_list[i][str(i+1)])