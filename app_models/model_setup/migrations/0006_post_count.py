# Generated by Django 4.1 on 2023-07-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_setup', '0005_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
