# Generated by Django 4.0.2 on 2022-04-14 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='password2',
        ),
    ]
