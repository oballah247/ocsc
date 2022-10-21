from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from django.views.generic import ListView
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User 
from django.contrib import messages
from frontend.models import *
from backend.forms import *
# Password Reset
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
 #  end


# Create your views here.

def dashboard(request):
    return render (request,'backend/dashboard.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  

        if user is not None:
            login(request, user)
            return render(request, 'backend/dashboard.html')
        else:
            messages.error(request, 'Username and Password do not match')
    return render (request,'frontend/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/backend/login/')
def add_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog_form = blog_form.save(commit=False)
            blog_form.user = request.user
            blog_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('backend:add_blog')
    else:
        blog_form = BlogForm()
    return render(request, 'backend/add_blog.html', {'blog_form': blog_form})

@login_required(login_url='/backend/login/')
def blog(request):
    blog_post = Blog.objects.order_by('-date')
    return render(request, 'backend/blog.html', {'blog':blog_post})

@login_required(login_url='/backend/login/')
def view_blog(request, view_id):
    post = Blog.objects.filter( id=view_id)
    return render(request, 'backend/view_blog.html', {'blog':post})

@login_required(login_url='/backend/login/')
def edit_blog(request, post_id):
    blog_post = get_object_or_404(Blog, id=post_id)
    if request.method == 'POST':
        editblog_form = EditBlogForm(request.POST, request.FILES,instance=blog_post)
        if editblog_form.is_valid():
            editblog_form = editblog_form.save(commit=False)
            editblog_form.user = request.user
            editblog_form.save()
            messages.success(request, 'Successfully Edited.')
            editblog_form = EditBlogForm(instance=blog_post)
    else:
        editblog_form = EditBlogForm(instance=blog_post)
    return render(request, 'backend/edit_blog.html', {'editblog_form': editblog_form})

@login_required(login_url='/backend/login/')
def delete_blog(request, delete_id):
    blog_record = get_object_or_404(Blog, id=delete_id)
    blog_record.delete()
    return redirect('backend:blog')

@login_required(login_url='/backend/login/')
def services(request):
    services_post = Services.objects.order_by('-date')
    return render(request, 'backend/services.html', {'services':services_post})

@login_required(login_url='/backend/login/')
def add_services(request):
    if request.method == 'POST':
        services_form = ServicesForm(request.POST, request.FILES)
        if services_form.is_valid():
            services_form = services_form.save(commit=False)
            services_form.user = request.user
            services_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('backend:add_services')
    else:
        services_form = ServicesForm()
    return render(request, 'backend/add_services.html', {'services_form': services_form})

@login_required(login_url='/backend/login/')
def edit_services(request, post_id):
    services_post = get_object_or_404(Services, id=post_id)
    if request.method == 'POST':
        editservices_form = EditServicesForm(request.POST, request.FILES,instance=services_post)
        if editservices_form.is_valid():
            editservices_form = editservices_form.save(commit=False)
            editservices_form.user = request.user
            editservices_form.save()
            messages.success(request, 'Successfully Edited.')
            editservices_form = EditServicesForm(instance=services_post)
    else:
        editservices_form = EditServicesForm(instance=services_post)
    return render(request, 'backend/edit_services.html', {'editservices_form': editservices_form})

@login_required(login_url='/backend/login/')
def view_services(request, view_id):
    services = Services.objects.filter( id=view_id)
    return render(request, 'backend/view_services.html', {'pst':services})

@login_required(login_url='/backend/login/')
def delete_services(request, delete_id):
    services_record = get_object_or_404(Services, id=delete_id)
    services_record.delete()
    return redirect('backend:services')

@login_required(login_url='/backend/login/')
def team(request):
    team_post = Team.objects.all()
    return render(request, 'backend/team.html', {'team':team_post})

@login_required(login_url='/backend/login/')
def add_team(request):
    if request.method == 'POST':
        team_form = TeamForm(request.POST, request.FILES)
        if team_form.is_valid():
            team_form = team_form.save(commit=False)
            team_form.user = request.user
            team_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('backend:add_team')
    else:
        team_form = TeamForm()
    return render(request, 'backend/add_team.html', {'team_form': team_form})

@login_required(login_url='/backend/login/')
def edit_team(request, team_id):
    team_post = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        editteam_form = EditTeamForm(request.POST, request.FILES,instance=team_post)
        if editteam_form.is_valid():
            editteam_form = editteam_form.save(commit=False)
            editteam_form.user = request.user
            editteam_form.save()
            messages.success(request, 'Successfully Edited.')
            editteam_form = EditTeamForm(instance=team_post)
    else:
        editteam_form = EditTeamForm(instance=team_post)
    return render(request, 'backend/edit_team.html', {'editteam_form': editteam_form})


@login_required(login_url='/backend/login/')
def view_team(request, view_id):
    team = Team.objects.filter( id=view_id)
    return render(request, 'backend/view_team.html', {'pst':team})

@login_required(login_url='/backend/login/')
def delete_team(request, delete_id):
    team_record = get_object_or_404(Team, id=delete_id)
    team_record.delete()
    return redirect('backend:team')

@login_required(login_url='/backend/login/')
def newsletter(request):
    newsletter = SubscribeModel.objects.order_by('-timestamp')
    return render(request, 'backend/newsletter.html', {'newsletter':newsletter})

def password_reset_request(request):
    if request.method == "POST":
        domain = request.headers['Host']
        password_reset_form = PasswordReset(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            # You can use more than one way like this for resetting the password.
            # ...filter(Q(email=data) | Q(username=data))
            # but with this you may need to change the password_reset form as well.
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "backend/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000/',
                        'site_name':'OCSC',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'josepholuwagbemi02@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordReset()
    return render(request=request, template_name="backend/password_reset.html",
                  context={"password_reset_form": password_reset_form})

@login_required(login_url='/backend/login/')
def change_password(request):
    if request.method == 'POST':
        change_password = PasswordChangeForm(data=request.POST,
        user=request.user)
        if change_password.is_valid():
            change_password.save()
            update_session_auth_hash(request, change_password.user)
            messages.success(request, 'Password changed successfully.')
    else:
        change_password = PasswordChangeForm(user=request.user)
    return render(request, 'backend/change_password.html', {'pass_key':change_password})

@login_required(login_url='/backend/login/')
def user_profile(request):
    return render(request, 'backend/user_profile.html')

@login_required(login_url='/backend/login/')
def edit_profile(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit_profile.html', {'edit_key':edit_form})
