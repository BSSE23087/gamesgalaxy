# Generated by Django 3.2.4 on 2021-08-16 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gameLogics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weeks', models.IntegerField()),
                ('miles', models.IntegerField()),
                ('ga', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gameLogics.gameaccount')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
