# Generated by Django 3.2.6 on 2022-06-15 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='mylist',
            fields=[
                ('id_list', models.AutoField(primary_key=True, serialize=False)),
                ('genre_id', models.IntegerField(blank=True, default=0)),
                ('categoryname', models.IntegerField(blank=True, default=0)),
                ('titles', models.CharField(max_length=100)),
            ],
        ),
    ]
