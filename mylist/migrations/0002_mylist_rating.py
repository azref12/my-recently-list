# Generated by Django 3.2.6 on 2022-06-21 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylist',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
