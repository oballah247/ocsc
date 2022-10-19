from django.urls import path
from django.conf.urls import url
from frontend import views 

app_name = 'frontend'

urlpatterns =[
    path('',views.about, name='about'),
    path('register/',views.register, name='register'),
    path('blog/',views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('team/',views.team, name='team'),
    path('contact/',views.contact, name='contact'),
    path('blog-post/<int:pk>', views.blog_post, name='blog_post'),

]