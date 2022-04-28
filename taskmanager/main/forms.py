from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileField
from django import forms
from django.forms import PasswordInput, EmailInput
from django.core.validators import RegexValidator


class PostForm(ModelForm):
    class Meta:
        model = Post1
        fields = ['name', 'news', 'author', 'password']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of status'
            }),

            'news': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Information of status'
            }),

            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of status'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            })
        }


class AddPostForm(forms.ModelForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-input', 'type': 'password'}))
    call_number = forms.IntegerField(label='Call_number)',
                                widget=forms.TextInput(attrs={'class': 'form-input', 'type': 'call_number'}))
    first_name = forms.CharField(label='First_name',)
    last_name = forms.CharField(label='Last_name',)
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-input'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Postusers
        fields = ('username', 'password', 'call_number', 'first_name', 'last_name', 'email', 'city', 'country')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     return cd['password']

    class AddPostForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)

        password2 = forms.CharField(widget=forms.PasswordInput)

        class Meta:
            model = Postusers

            fields = '__all__'

        def clean_password2(self):
            cd = self.cleaned_data

            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')

            return cd['password']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))



class EmailForm(forms.Form):
        email = forms.EmailField(label='Пайдаланушы аты')
        subject = forms.CharField(max_length=100)
        attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        message = forms.CharField(widget=forms.Textarea)
