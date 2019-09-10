# Generated by Django 2.2.5 on 2019-09-05 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0014_auto_20190905_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='followers',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twitter_followers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twitter_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
