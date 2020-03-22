import json

def is_json(myJson):
    try:
        json_object = json.loads(myJson)
    except ValueError as e:
        return False
    return True
