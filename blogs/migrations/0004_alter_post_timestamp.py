# Generated by Django 3.2.5 on 2021-08-12 09:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
