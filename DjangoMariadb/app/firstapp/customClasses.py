import json
from django.http import JsonResponse
import string
import secrets
import random
from firstapp.models import Movie,ApiUsers

class checkJson():

    def __init__(self):
        return None

    def isJson(self,myjson):
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            response_data = {}
            response_data['result'] = 'error'
            response_data['message'] = 'Invalid Json'
            return response_data
        return True

class ApiKey():

    ApiLength = 32
    ApiLengthC = 64
    def __init__(self):
        return None

    def check(self,request):
        try:
            apiKey = request.headers["user-api-key"]
            return True
        except KeyError:
            response_data = {}
            response_data['result'] = 'error'
            response_data['message'] = 'user-api-key is required'
            return response_data
        #return True

    def generate_key_simple(self):
        return secrets.token_hex(self.ApiLength)

    def generate_key_complex(self):
        char_set = string.ascii_letters + string.punctuation
        urand = random.SystemRandom()
        return ''.join([urand.choice(char_set) for _ in range(self.ApiLengthC)])

class ClientChecks():

    def __init__(self):
        return None

    def CheckJsonAttrs(self, json_data):
        response_data = {}
        missingAttr = False
        missingAttrMsg = ""

        if 'user' not in json_data:
            missingAttr = True
            missingAttrMsg = "user is required"
        elif 'password' not in json_data:
            missingAttr = True
            missingAttrMsg = "password is required"

        if missingAttr == True:
            response_data['result'] = 'error'
            response_data['message'] = missingAttrMsg
            return JsonResponse(response_data, status=401)
        else:
            return True

    def CheckUserExists(self, json_data):
        response_data = {}
        try:
            userObj = ApiUsers.objects.get(user = json_data['user'])
            return True, userObj
        except Exception as e:
            response_data['result'] = 'error'
            response_data['message'] = 'The user does not exist or the password is incorrect'
            return False, JsonResponse(response_data,status=401)
