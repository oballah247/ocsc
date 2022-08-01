from django.urls import path
from django.conf.urls import url
from frontend import views 


app_name = 'frontend'

urlpatterns =[
    path('index/',views.index, name='index'),
    path('bout/',views.about, name='about'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('Blog/',views.blog, name='Blog'),
    path('portfolio_details/',views.portfolio_details, name='portfolio_details'),
    path('Services/', views.services, name='services'),
    path('team/',views.team, name='team'),
    path('contact/',views.contact, name='contact'),

]