from django.db import models


class servers(models.Model):
  task_event_type = models.CharField(max_length=30)
  task_start_program_time = models.TimeField()
  task_start_actual_time = models.TimeField()
  number_of_servers_running = models.CharField(max_length=10)
  clock_wall_color = models.CharField(max_length=50)
  clock_face_color = models.CharField(max_length=50)
  clock_hand_color = models.CharField(max_length=50)
