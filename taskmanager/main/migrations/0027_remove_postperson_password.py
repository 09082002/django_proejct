# Generated by Django 4.0.2 on 2022-04-16 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_postperson_delete_postpersons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postperson',
            name='password',
        ),
    ]
