# Generated by Django 3.1.2 on 2020-11-08 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_paid_until'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='paid_until',
        ),
    ]