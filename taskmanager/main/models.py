from django.core.exceptions import ValidationError
from django.db import models
from django.forms import forms
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class Persons(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_birth = models.DateField()

    def __str__(self):
        return self.first_name


class National(models.Model):
    foods_name = models.CharField(max_length=50)
    content = models.TextField(max_length=450)

    def __str__(self):
        return self.foods_name


class Medical(models.Model):
    title = models.CharField(max_length=50)
    information = models.TextField(max_length=450)

    def __str__(self):
        return self.information


class Post1(models.Model):
    name = models.CharField('Название', max_length=50)
    news = models.CharField('Информация', max_length=500)
    file = models.FileField()
    author = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/news_home/{self.id}'


class Postusers(models.Model):
    username = models.CharField(max_length=250, verbose_name="Username")
    email = models.EmailField( verbose_name="email")
    password = models.CharField(max_length=20, verbose_name='password')
    first_name = models.CharField(max_length=30, verbose_name="First name", validators=[alphanumeric])
    last_name = models.CharField(max_length=30, verbose_name='Last name', validators=[alphanumeric])
    city = models.CharField(max_length=30, verbose_name="city", )
    address = models.CharField(max_length=30, verbose_name="address")
    number = models.IntegerField(verbose_name="call_number", default = 1)

    def __str__(self):
        return self.username



    # def clean(self):
    #     cleaned_data = super().clean()
    #     first_name = cleaned_data.get('first_name')
    #     last_name = cleaned_data.get('last_name')


    # username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # password2 = forms.CharField(label='Re-enter password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # city = forms.CharField(label='Cities', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-input'}))

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_slug': self.slug})




