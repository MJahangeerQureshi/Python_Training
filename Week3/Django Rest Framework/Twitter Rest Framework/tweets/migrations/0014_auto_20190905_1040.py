# Generated by Django 2.2.5 on 2019-09-05 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0013_auto_20190905_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='followers',
            field=models.ManyToManyField(related_name='twitter_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twitter_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Follower',
        ),
    ]
