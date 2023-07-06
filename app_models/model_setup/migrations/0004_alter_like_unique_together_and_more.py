# Generated by Django 4.1 on 2023-07-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_setup', '0003_post_likes'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
