# Generated by Django 4.1.4 on 2023-09-08 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='greroboticsmodel',
            old_name='slug',
            new_name='slugs',
        ),
    ]
