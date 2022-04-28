# Generated by Django 4.0.2 on 2022-04-16 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_postpersons_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('news', models.CharField(max_length=500, verbose_name='Информация')),
                ('file', models.FileField(upload_to='')),
                ('author', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Postpersons',
        ),
        migrations.DeleteModel(
            name='Userinfos',
        ),
    ]
