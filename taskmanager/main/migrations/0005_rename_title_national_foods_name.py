# Generated by Django 4.0.2 on 2022-03-03 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_medical_national_delete_medicine_delete_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='national',
            old_name='title',
            new_name='foods_name',
        ),
    ]
