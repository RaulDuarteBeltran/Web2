from firstapp.models import Movie,ApiUsers

#IMPORT LIBRARIRES/FUNCTIONS
#from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
from firstapp.JsonCheckClass import *
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from firstapp.JsonCheck import *
from firstapp.customClasses import *

def makepassword(request, password):
    hashPassword = make_password(password)
    response_data = {}
    response_data['password'] = hashPassword
    return JsonResponse(response_data, status=200)


def login(request):
    #VALIDATE METHOD
    if request.method == 'POST':
        #DECLARE RESPONSE
        response_data = {}
        #CHECK JSON STRUCTURE
        isJson = is_json(request.body)
        if isJson == True:
            json_data = json.loads(request.body)
            #CHECK JSON CONTENT
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
            #CHECK IF USER EXITST
            try:
                userObj = ApiUsers.objects.get(user = json_data['user'])
            except Exception as e:
                response_data['result'] = 'error'
                response_data['message'] = 'The user does not exist or the password is incorrect'
                return JsonResponse(response_data,status=401)
            #TAKE PASSWORD OF THE USER
            password = json_data['password']
            hassedPassword = userObj.password
            #CHECK IF PASSWORD IS CORRECT
            passwordIsCorrect = check_password(password, hassedPassword)
            if passwordIsCorrect == False:
                response_data['result'] = 'error'
                response_data['message'] = 'The user does not exist or the password is incorrect'
                return JsonResponse(response_data, status = 401)
            #CHECK IF USER HAS API-KEY
            if userObj.api_key==None:
                newApiKey = ApiKey().generate_key_complex()
                userObj.api_key = newApiKey
                userObj.save()
            #RETURN RESPONSE
            response_data['result'] = 'success'
            response_data['message'] = 'Valid Credentials'
            response_data['userApiKey'] = userObj.api_key
            return JsonResponse(response_data,status=200)
        else:
            response_data['result'] = 'error'
            response_data['message'] = 'Invalid Json'
            return JsonResponse(response_data, status=400)

    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Invalid Request'
        return JsonResponse(response_data, status=400)
