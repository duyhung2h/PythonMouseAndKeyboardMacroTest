import json
class JSONToPyList():
    def __init__(self):
        self = self
        self.name_list = []
    def start(self):
        # Open existing JSON file!
        f = open("exported_JSON/perfected JSON/JSON_modded_DOTD.json", "r")
        jsonStr = f.read()
        data = json.loads(jsonStr)
        name_list = data['items']

        f2 = open("exported_JSON/perfected JSON/JSON_vanilla_DOI.json", "r")
        jsonStr2 = f2.read()
        data2 = json.loads(jsonStr2)
        name_list2 = data2['items']
        # print(len(name_list))
        for i in range (0, len(name_list)-1, 1):
            # print(name_list2[i][str(i)])
            if name_list2[i][str(i)] == '0' or int(name_list[i][str(i)]) <= 499999:
                self.name_list.append(
                    {str(i): name_list2[i][str(i)]})
            elif int(name_list[i][str(i)]) > 499999:
                self.name_list.append(
                    {str(i): name_list[i][str(i)]})

        # write to JSON file!
        jsonStrEnd = json.dumps({'items': self.name_list})
        fEnd = open("exported_JSON/perfected JSON/JSON_modded_DOI.json", "a")
        # f = open("exported_JSON/JSON_new.json", "a")
        fEnd.truncate(0)
        fEnd.write(jsonStrEnd)
        fEnd.close()
        print('done!')