# Generated by Django 5.0.6 on 2024-08-25 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0003_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolioapp.image'),
        ),
    ]
