from django.shortcuts import render, HttpResponse
from .models import Estados
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import json
from firstapp.JsonCheck import *
from firstapp.JsonCheckClass import revisarJson

def results(request, id):
    if request.method == 'GET':
        response_data = {}
        try:
            obj = Estados.objects.get(id=id)
            response_data['result'] = 'success'
            response_data['name'] = obj.name
            response_data['clave'] = obj.clave
            response_data['abrev'] = obj.abrev
            response_data['riskIndex'] = obj.risk
            return JsonResponse(response_data, status=200)
        except Estados.DoesNotExist:
            response_data['result'] = 'error'
            response_data['message'] = 'No se encontro el id'
            return JsonResponse(response_data, status=400)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Invalid Request'
        return JsonResponse(response_data, status=403)

def states(request):
    if request.method == 'GET':
        response_data = {}
        response_data['estados'] = {}
        cont = 0
        for obj in Estados.objects.all():
            response_data["estados"][cont] = {}
            Estado = response_data["estados"][cont]
            Estado['name'] = obj.name
            Estado['clave'] = obj.clave
            Estado['abrev'] = obj.abrev
            Estado['riskIndex'] = obj.risk
            cont += 1
        response_data['result'] = 'success'
        return JsonResponse(response_data,status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Invalid Request'
        return JsonResponse(response_data, status=403)
