from django.urls import path

from . import views
from . import EjemploStates
from .Views import ClientView

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /1.0/5/
    path('view/<int:id>/', views.results, name='results'),
    path('client/getAllTasks/', views.getAllTasks, name='getAllTasks'),
    path('client/createTask/', views.createTask, name='createTask'),
    path('task/completeTask/', views.completeTask, name='completeTask'),
    path('task/deleteTask/',views.deleteTask, name='deleteTask'),

    #Ejemplo Estados
    path('states/', EjemploStates.states, name='states'),
    path('states/<int:id>/',EjemploStates.results, name='getState'),

    #Parte de movies
    path('client/login', views.logUser, name='logUser'),
    path('client/movies', views.getMovies, name='getMovies'),

    #Parte de Clientes
    path('generate_password/<str:password>', ClientView.makepassword, name='makepassword'),
    path('client/login', ClientView.login, name='login'),


]
