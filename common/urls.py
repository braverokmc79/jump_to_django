from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    
    path('', views.logout_view, name='logout'),  # '/' 에 해당되는 path
    path('signup/', views.signup, name='signup'),
]
