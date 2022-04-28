# Generated by Django 4.0.2 on 2022-04-16 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_postpersons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postperson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250, verbose_name='Username')),
                ('email', models.EmailField(max_length=30, verbose_name='email')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('city', models.CharField(max_length=30, verbose_name='city')),
                ('address', models.CharField(max_length=30, verbose_name='address')),
            ],
        ),
        migrations.DeleteModel(
            name='Postpersons',
        ),
    ]