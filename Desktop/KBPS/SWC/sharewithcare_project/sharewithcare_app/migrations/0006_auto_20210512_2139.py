# Generated by Django 3.1.7 on 2021-05-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharewithcare_app', '0005_auto_20210512_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='add2',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='add3',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]
