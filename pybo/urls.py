from debug_toolbar import APP_NAME
from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/',views.detail , name='detail'),
]




