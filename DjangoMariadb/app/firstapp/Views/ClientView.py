from firstapp.models import Movie,ApiUsers

#IMPORT LIBRARIRES/FUNCTIONS
#from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
from firstapp.JsonCheckClass import *
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from firstapp.JsonCheck import *

def makepassword(request, password):
    hashPassword = make_password(password)
    response_data = {}
    response_data['password'] = hashPassword
    return JsonResponse(response_data, status=200)


def login(request):

    #VALIDATE METHOD
    if request.method == 'POST':
        #DECLARE RESPONSE
        responseData = {}
        #CHECK JSON STRUCTURE
        isJson = is_json(request.body)
        if isJson == True:
            Json_data = json.loads(request.body)
            #CHECK JSON CONTENT
            missingAttr = False
            missingAttrMsg = ""

            if 'user' not in json_data:
                missingAttr = True
                missingAttrMsg = "User is required"
            elif 'password' not in json_data:
                missingAttr = True
                missingAttrMsg = "Password is required"

            if missingAttr == True:
                response_data['result'] = 'error'
                response_data['message'] = missingAttrMsg
                return JsonResponse(response_data, status=401)
            #CHECK IF USER EXITST
            try:
                userObj = ApiUsers.objects.get(user = json_data['user'])
            except Entry.DoesNotExist as e:
                response_data['result'] = 'error'
                response_data['message'] = 'The user does not exist or the password is incorrect'
                return JsonResponse(response_data,status=401)
            #TAKE PASSWORD OF THE USER
            password = userObj.password
            #CHECK IF PASSWORD IS CORRECT


            #CHECK IF USER HAS API-KEY
            #obj.api_key = newApiKey
            #obj.save()


            #RETURN RESPONSE
        else:
            response_data['result'] = 'error'
            responseData['message'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)

    else:
        responseData = {}
        responseData['result'] = 'error'
        responseData['message'] = 'Invalid Request'
        return JsonResponse(responseData, status=400)
