# Generated by Django 4.0.1 on 2022-06-29 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_userp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userp',
            old_name='c_id',
            new_name='id',
        ),
    ]
