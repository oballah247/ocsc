from django.shortcuts import render, redirect, get_object_or_404
# from requests import request
from frontend.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import messages
from frontend.form import *


# Create your views here.

def index (request):
    ser = Services.objects.all()[:6]
    return render (request,'frontend/index.html', {'services':ser})
    
def about (request):
    about = About.objects.all()
    return render (request,'frontend/about.html',{'aba':about})


def team (request):
    team = Team.objects.all()
    return render (request,'frontend/team.html', {'team':team})
   

def register (request):
    if request.method == 'POST':
        register_form = RegForm(request.POST)
        if  register_form.is_valid():
            register_form.save()
    else:
            register_form =RegForm()
    return render(request, 'frontend/Register.html',{'reg':register_form})


# def innerpage(request):
#     return render (request,'frontend/inner-page.html')


    
def login(request):
    return render (request,'frontend/Login.html',{'login':login} )

    
def blog(request):
    blogs = Blog.objects.all()
    return render (request,'frontend/Blog.html',{'blog':blogs} )


def blog_post(request, pk):
    single_post = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(post=pk).order_by('-timestamp')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = single_post
            comment.save()
            return redirect('frontend:blog_post', pk=single_post.pk)
            single_post = {'form': form, 'most_recent': most_recent,}
    else:
        form = CommentForm()
    return render(request, 'frontend/blog-details.html', {'comm':comments, 'form':form, 'sipst':single_post})

def services(request):
    ser = Services.objects.all()
    return render (request, 'frontend/services.html',{'services':ser} )

def contact (request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if  contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thanks for contacting OCSC')
    else:
        contact_form =ContactForm()
    return render (request, 'frontend/contact.html',{'cont':contact_form} )



