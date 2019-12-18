from django.urls import path,re_path
from . import views as main_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
  path('',main_views.index,name='index'),
  re_path(r'api/get/details/$',csrf_exempt(main_views.sendData.as_view()),name='startask'),
  re_path(r'api/get/report/$',csrf_exempt(main_views.sendReport.as_view()),name='sendReport'),
  re_path(r'api/startime/$',csrf_exempt(main_views.startime.as_view()),name='startime'),
]


if settings.DEBUG:
  urlpatterns += static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
  )
