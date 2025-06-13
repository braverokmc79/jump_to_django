from debug_toolbar import APP_NAME
from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),    
    path('question/create/', views.question_create, name='question_create'),     
    path('<int:question_id>/',views.detail , name='detail'),    
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    
    
    
]




