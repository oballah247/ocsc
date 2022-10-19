# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from frontend.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from backend.forms import *
from django.conf import settings 

# Create your views here.

def index (request):
    ser = Services.objects.all()[:3]
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('index')
    else:
        subscribe_form = SubscribeForm()
    return render (request,'frontend/index.html', {'services':ser, 'subscribe_form':subscribe_form})
    
def about (request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('index')
    else:
        subscribe_form = SubscribeForm()
    return render (request,'frontend/about.html', {'subscribe_form':subscribe_form})


def team (request):
    team = Team.objects.all()
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('index')
    else:
        subscribe_form = SubscribeForm()
    return render (request,'frontend/team.html', {'team':team, 'subscribe_form':subscribe_form})
   

def register (request):
    if request.method == 'POST':
        register_form = RegForm(request.POST)
        if  register_form.is_valid():
            register_form.save()
    else:
        register_form =RegForm()
    return render(request, 'frontend/register.html',{'reg':register_form})


# def innerpage(request):
#     return render (request,'frontend/inner-page.html')


    
def blog(request):
    blogs = Blog.objects.all()
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('index')
    else:
        subscribe_form = SubscribeForm()
    return render (request,'frontend/Blog.html',{'blog':blogs, 'subscribe_form':subscribe_form} )


def blog_post(request, pk):
    single_post = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(post=pk).order_by('-timestamp')
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('index')
    else:
        subscribe_form = SubscribeForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = single_post
            comment.save()
            return redirect('frontend:blog_post', pk=single_post.pk)
            single_post = {'form': form, 'most_recent': comments,}
    else:
        form = CommentForm()
    return render(request, 'frontend/blog-details.html', {'comm':comments, 'form':form, 'sipst':single_post, 'subscribe_form':subscribe_form})

def services(request):
    ser =  Services.objects.order_by('-date')
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('index')
    else:
        subscribe_form = SubscribeForm()
    return render (request, 'frontend/services.html',{'services':ser, 'subscribe_form':subscribe_form} )

def contact (request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('index')
    else:
        subscribe_form = SubscribeForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if  contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thanks for contacting OCSC')
    else:
        contact_form =ContactForm()
    return render (request, 'frontend/contact.html',{'cont':contact_form, 'subscribe_form':subscribe_form} )



