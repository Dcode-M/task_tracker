from django.urls import path
from . import views as main_views


urlpatterns = [
  path('',main_views.index,name='index')
]