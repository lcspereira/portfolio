# Generated by Django 5.0.6 on 2024-08-21 02:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=100)),
                ('title_pt', models.CharField(max_length=100)),
                ('description_en', models.TextField()),
                ('description_pt', models.TextField()),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioapp.image')),
                ('technologies', models.ManyToManyField(to='portfolioapp.technology')),
            ],
        ),
    ]
