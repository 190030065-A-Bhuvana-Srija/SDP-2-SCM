# Generated by Django 3.1.5 on 2021-01-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_seller_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='max_kg',
            field=models.IntegerField(default=0),
        ),
    ]
