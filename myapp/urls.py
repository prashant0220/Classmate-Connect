from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('Registered/', views.success_register, name='register_success'),
]