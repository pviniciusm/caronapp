# Generated by Django 2.0.1 on 2018-01-04 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180104_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puser',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='puser',
            name='lname',
        ),
    ]
