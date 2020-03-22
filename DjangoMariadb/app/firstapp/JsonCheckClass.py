import json

class revisarJson():

    hol = 1

    def __init__(self):
        return None

    def isJson(self,myJson):
        try:
            json_object = json.loads(myJson)
        except ValueError as e:
            return False
        return True
