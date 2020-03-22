from firstapp.models import Movie,ApiUsers

#IMPORT LIBRARIRES/FUNCTIONS
#from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
from firstapp.JsonCheckClass import *
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password

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


        #CHECK JSON CONTENT


        #CHECK IF USER EXITST


        #TAKE PASSWORD OF THE USER

        #CHECK IF PASSWORD IS CORRECT


        #CHECK IF USER HAS API-KEY
        #obj.api_key = newApiKey
        #obj.save()


        #RETURN RESPONSE

    else:
        responseData = {}
        responseData['result'] = 'error'
        responseData['message'] = 'Invalid Request'
        return JsonResponse(responseData, status=400)
