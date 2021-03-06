# Generated by Django 3.1.7 on 2021-05-15 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharewithcare_app', '0010_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='accepted_eula',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite_animal',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
