# Generated by Django 2.2.5 on 2019-09-04 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0004_auto_20190904_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.CharField(max_length=280)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
