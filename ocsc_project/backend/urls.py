from unicodedata import name
from django.urls import path
from django.conf.urls import url
from backend import views


urlpatterns =[
      
        path('dashboard/', views.dashboard, name='dashboard')
]