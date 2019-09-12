# Generated by Django 2.2.5 on 2019-09-11 16:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0015_auto_20190905_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='followers',
        ),
        migrations.AddField(
            model_name='follower',
            name='followers',
            field=models.ManyToManyField(related_name='twitter_followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
