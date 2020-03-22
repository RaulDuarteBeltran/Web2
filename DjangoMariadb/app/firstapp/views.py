from django.shortcuts import render, HttpResponse
from .models import Estados
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import json
from firstapp.JsonCheck import *
from firstapp.JsonCheckClass import revisarJson

def index(request):
    if request.method == 'GET':
        #return HttpResponse("HOLA")
        response_data = {}
        # try:
        #     json_object = json.loads(request.body)
        # except ValueError as e:
        #     response_data = {}
        #     response_data['result'] = 'error'
        #     response_data['message'] = 'Json inválido'
        #     return JsonResponse(response_data,status=401)
        checkJson = revisarJson()
        check = checkJson.isJson(request.body)

        isJson = is_json(request.body)

        if isJson == True:
            #response_data['result'] = 'success'
            #response_data['message'] = 'Correcto'
            #return JsonResponse(response_data,status=200)
            json_data = json.loads(request.body)
            attr_error = False
            attrErrorMsg = ""
            if 'var1' not in json_data:
                attr_error = True
            elif 'var2' not in json_data:
                attr_error = True
            elif 'var3' not in json_data:
                attr_error = True

            if attr_error == True:
                attrErrorMsg = "Falta un campo"
                response_data['result'] = 'error'
                response_data['message'] = attrErrorMsg
                return JsonResponse(response_data, status=400)
            else:
                response_data['result'] = 'success'
                response_data['message'] = 'Todo bien'
                return JsonResponse(response_data, status=200)
        else:
            response_data['result'] = 'error'
            response_data['message'] = 'Metodo inválido'
            return JsonResponse(response_data,status=401)
        #return HttpResponse("Adios")

def results(request, id):
    #Event.objects.get(id=1)
    event_list = Estados.objects.all()
    return HttpResponse("You're looking at %s." % event_list[0].name)
    #return HttpResponse("You're looking at %s." % id)

def getAllTasks(request):
    json_data = json.loads(request.body)
    if request.method == 'GET':
        #return HttpResponse("HOLA")
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Método válido'
        return JsonResponse(response_data,status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Metodo inválido'
        return JsonResponse(response_data,status=401)
        #return HttpResponse("Adios")

def createTask(request):
    if request.method == 'POST':
        #return HttpResponse("HOLA")
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Método válido'
        return JsonResponse(response_data,status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Invalid Requiest'
        return JsonResponse(response_data,status=401)
        #return HttpResponse("Adios")

def completeTask(request):
    if request.method == 'PUT':
    #return HttpResponse("HOLA")
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Método válido'
        return JsonResponse(response_data,status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Invalid Requiest'
        return JsonResponse(response_data,status=401)
    #return HttpResponse("Adios")return HttpResponse("COMPLETE TASK")

def deleteTask(request):
    if request.method == 'DELETE':
        #return HttpResponse("HOLA")
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Método válido'
        return JsonResponse(response_data,status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Invalid Requiest'
        return JsonResponse(response_data,status=401)
        #return HttpResponse("Adios")

def logUser(request):
    if request.method == 'POST':
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Método válido'
        return JsonResponse(response_data,status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Metodo inválido'
        return JsonResponse(response_data,status=401)

def getMovies(request):
    if request.method == 'POST':
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Método válido'
        return JsonResponse(response_data,status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Metodo inválido'
        return JsonResponse(response_data,status=401)
