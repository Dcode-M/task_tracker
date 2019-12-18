from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import updates 
import datetime
from datetime import timedelta
from .models import servers
import random
import time
import threading


# home view function 
def index(request):
  return render(request,'index.html')


# generates the number of servers started
def calculateServersStarted():

  n_servers_started = random.randrange(10,21)

  return n_servers_started

# generates the number of servers stoped
def calculateServersStoped(k):

  n_servers_stoped = random.randrange(5,k)

  return n_servers_stoped

# generates the number of servers running at each point
def serversReport(n,k):

  return n-k

# generates a color-code
def getColorCode():

  color = ['#'+''.join(random.choice('0123456789ABCDEF') for i in range(6))]

  return color[0]


class runservers(object):
  called = False

  def __init__(self):
    thread = threading.Thread(target=self.run, args=())
    thread.daemon = True                            
    thread.start() 
                        

  def run(self):
    timeoutSeconds = 60
    program_time = datetime.datetime(2019,12,19,12,00,00)
    current_time = datetime.datetime(2019,6,13,10,00,00)
    while timeoutSeconds > 0:

      time.sleep(30)

      program_time += timedelta(seconds = 30)
      current_time += timedelta(seconds = 30)
      task_event_type = 'START'
      number_of_servers_running = calculateServersStarted()
      clock_wall_color = getColorCode()
      clock_face_color = getColorCode()
      clock_hand_color = getColorCode()

      server_status = servers(
        task_event_type = task_event_type,
        task_start_program_time = program_time,
        task_start_actual_time = current_time,
        number_of_servers_running = number_of_servers_running,
        clock_wall_color = clock_wall_color,
        clock_face_color = clock_face_color,
        clock_hand_color = clock_hand_color
      )
      server_status.save()


      time.sleep(10)
      started_servers = servers.objects.order_by('-pk').first()

      program_time += timedelta(seconds=10)
      current_time += timedelta(seconds=10)
      task_event_type = 'STOP'
      number_of_servers_running = calculateServersStoped(int(started_servers.number_of_servers_running))
      clock_wall_color = getColorCode()
      clock_face_color = getColorCode()
      clock_hand_color = getColorCode()

      server_status = servers(
        task_event_type = task_event_type,
        task_start_program_time = program_time,
        task_start_actual_time = current_time,
        number_of_servers_running = number_of_servers_running,
        clock_wall_color = clock_wall_color,
        clock_face_color = clock_face_color,
        clock_hand_color = clock_hand_color
      )
      server_status.save()

      # get servers
      started_servers = servers.objects.order_by('-pk').first()
      stoped_servers = servers.objects.get(pk = started_servers.pk - 1)

      time.sleep(10)
      program_time += timedelta(seconds=10) 
      current_time += timedelta(seconds=10)
      task_event_type = 'REPORT'
      number_of_servers_running = serversReport(int(started_servers.number_of_servers_running),int(stoped_servers.number_of_servers_running))
      clock_wall_color = getColorCode()
      clock_face_color = getColorCode()
      clock_hand_color = getColorCode()

      server_status = servers(
        task_event_type = task_event_type,
        task_start_program_time = program_time,
        task_start_actual_time = current_time,
        number_of_servers_running = number_of_servers_running,
        clock_wall_color = clock_wall_color,
        clock_face_color = clock_face_color,
        clock_hand_color = clock_hand_color
      )
      server_status.save()

      program_time += timedelta(seconds = 50)
      current_time += timedelta(seconds = 50)

      timeoutSeconds -= 10

    

class sendData(APIView):
  '''
  Sends back the displa message to the frontend
  '''
  def get(self,request,format = None,*args,**kwargs):
    # runservers()
    try:
      return_value = servers.objects.order_by('-pk').first()
      serializer = updates(return_value)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)



class sendReport(APIView):
  '''
  Sends the sample computation to the front end using the respective api
  '''
  def get(self,request,format = None,*args,**kwargs):
    try:
      reports = servers.objects.all()
      serializer = updates(reports,many=True)
      return Response(serializer.data,status = status.HTTP_200_OK)
      
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)


class startime(APIView):
  def get(self,request,format = None,*args,**kwargs):
    runservers()
    return Response(status = status.HTTP_200_OK)

