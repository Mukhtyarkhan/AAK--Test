# Generated by Django 5.1.7 on 2025-03-24 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='lables',
            new_name='labels',
        ),
    ]
