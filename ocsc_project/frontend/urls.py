from django.urls import path
from django.conf.urls import url
from frontend import views 


app_name = 'frontend'

urlpatterns =[
    path('index/',views.index, name='index'),
    path('bout/',views.about, name='about'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('blog/',views.blog, name='Blog'),
    path('services/', views.services, name='services'),
    path('team/',views.team, name='team'),
    path('contact/',views.contact, name='contact'),
      path('blog-post-page/<int:pk>', views.blog_post, name='blog_post'),

]