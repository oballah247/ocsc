from django.shortcuts import render
from frontend.models import *

# Create your views here.

def dashboard(request):
    return render (request,'backend/dashboard.html')
