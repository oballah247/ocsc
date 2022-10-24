import email
from email.headerregistry import Address
from tkinter import Message
from tkinter.tix import Form
from turtle import title
from typing import Type
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=20, verbose_name='Team Member Name')
    image = models.FileField(null=True, blank=True,upload_to='uploads/pics')
    discription = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __srf__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=20, verbose_name='Service Name')
    image = models.FileField(null=True, blank=True,upload_to='uploads/pics')
    discription = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  
    def __srf__(self):
        return self.name

class Contact(models.Model):
    address = models.CharField(max_length=100)
    email= models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __srf__(self):
        return self.first_name

class Blog(models.Model):
    title = models.CharField(max_length=40, verbose_name='BLog Title')
    image = models.FileField(null=True, blank=True,upload_to='uploads/pics')
    discription = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150, verbose_name= 'User Name')
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(verbose_name= 'Content')
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class SubscribeModel(models.Model):
    email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
    timestamp = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.email