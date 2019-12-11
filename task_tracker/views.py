from django.shortcuts import render
from django.http import HttpResponse


# home view function
def index(request):
  return HttpResponse('Lets go to work Denis')
