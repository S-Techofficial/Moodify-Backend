# Generated by Django 3.1.2 on 2020-11-07 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_is_subscribed'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='paid_until',
            field=models.DateField(blank=True, null=True),
        ),
    ]