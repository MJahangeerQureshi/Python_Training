# Generated by Django 2.2.5 on 2019-09-16 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20190916_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='twitter_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
