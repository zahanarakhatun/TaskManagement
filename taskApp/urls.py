from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login'), name='home'),
    
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]