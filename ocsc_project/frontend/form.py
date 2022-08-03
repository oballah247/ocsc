from cProfile import label
from tkinter import Widget
# from form import models
from frontend.models import *
from  django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core import validators


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    email = forms.EmailField(label='Email :',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    address = forms.CharField(label='Address :', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter:Address'}))
    
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your message',
        'id': 'usercomment',
        'rows': '4'
    }))
    
    class Meta():
     model = Contact
     fields = ['first_name', 'last_name', 'email', 'address', 'message']


class CommentForm(forms.ModelForm):
    user_name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    comment_content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        exclude = ['user', 'post']
        # fields = ('content', )


class RegForm(UserCreationForm):
    username = forms.CharField(label='Username :', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    email = forms.EmailField(label='Email :',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    password1 = forms.CharField(label='Enter Password :', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    
    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            return user



















