# Generated by Django 2.0.1 on 2018-01-04 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180102_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puser',
            name='name',
        ),
        migrations.AddField(
            model_name='puser',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='puser',
            name='fname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='puser',
            name='lname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
