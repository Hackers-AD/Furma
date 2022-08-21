# Generated by Django 3.0.4 on 2020-03-22 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20200322_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='image',
            field=models.FileField(blank=True, upload_to='product/group/images'),
        ),
        migrations.AlterField(
            model_name='option',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, unique=True),
        ),
    ]
