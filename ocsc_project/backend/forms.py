from django import forms
from frontend.models import *
from django.core import validators
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import(PasswordResetForm, SetPasswordForm, UserChangeForm, UserCreationForm)


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

class BlogForm(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ['image', 'title','discription',]
        exclude = [ 'user', 'date']

        widgets = { 
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'News'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),  
        }

class EditBlogForm(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ['image', 'title','discription',]
        exclude = [ 'user', 'date']

        widgets = { 
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'News'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),  
        }

class ServicesForm(forms.ModelForm):
    class Meta():
        model = Services
        fields = ['image', 'name','discription',]
        exclude = [ 'user', 'date']

        widgets = { 
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'News'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),  
        }

class EditServicesForm(forms.ModelForm):
    class Meta():
        model = Services
        fields = ['image', 'name','discription',]
        exclude = [ 'user', 'date']

        widgets = { 
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'News'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),  
        }
class TeamForm(forms.ModelForm):
    class Meta():
        model = Team
        fields = ['image', 'name','discription',]
        exclude = [ 'user']

        widgets = { 
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'News'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),  
        }
class EditTeamForm(forms.ModelForm):
    class Meta():
        model = Team
        fields = ['image', 'name','discription',]
        exclude = [ 'user']

        widgets = { 
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'News'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),  
        }

class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    class Meta:
        model = SubscribeModel
        fields = ['email']

class PasswordReset(PasswordResetForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    
class SetPassword(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Confirm Password'}))

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Old Password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])














