from email.policy import HTTP
from django.shortcuts import render, redirect, get_object_or_404
# from requests import request
from frontend.models import *
# from ocsc_project import frontend
from frontend.form import *


# Create your views here.

def index (request):
    return render (request,'frontend/index.html')
    
def about (request):
    about = about.objects.all()
    return render (request, 'frontend/about.html',{'aba':about} )


def team (request):
    team = Team.objects.all()
    return render (request,'frontend/index.html', {'team':team})
   

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

def portfolio_details(request):
    pee = Services.objects.all()
    return render (request,'frontend/portfolio-details.html',{'port':pee} )
    
def login(request):
    return render (request,'frontend/Login.html',{'login':login} )

    
def blog(request):
    blogs = Blog.objects.all()
    return render (request,'frontend/Blog.html',{'blog':blogs} )


def services(request):
    ser = Services.objects.all()
    return render (request, 'frontend/services.html',{'services':ser} )

def contact (request):
    contact = Contact.objects.all()
    return render (request, 'frontend/contact.html',{'cont':contact} )



