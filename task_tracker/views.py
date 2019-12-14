from django.shortcuts import render
from django.http import HttpResponse


# home view function
def index(request):
  return render(request,'index.html')
