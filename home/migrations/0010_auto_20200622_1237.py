# Generated by Django 3.0.7 on 2020-06-22 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200621_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='sub_total',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='total',
        ),
    ]
