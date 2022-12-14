# Generated by Django 3.0.4 on 2020-03-22 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20200322_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='code',
            field=models.SlugField(max_length=128),
        ),
        migrations.CreateModel(
            name='ProductAttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_text', models.TextField(blank=True, null=True)),
                ('value_integer', models.IntegerField(blank=True, db_index=True, null=True)),
                ('value_boolean', models.NullBooleanField(db_index=True)),
                ('value_float', models.FloatField(blank=True, db_index=True, null=True)),
                ('value_richtext', models.TextField(blank=True, null=True)),
                ('value_date', models.DateField(blank=True, db_index=True, null=True)),
                ('value_datetime', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('value_file', models.FileField(blank=True, max_length=255, null=True, upload_to='product/attributes/')),
                ('value_image', models.ImageField(blank=True, max_length=255, null=True, upload_to='product/attributes/')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productattrs', to='catalogue.ProductAttribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productattrvalues', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('image', models.FileField(upload_to='product/group/images')),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.ProductGroup')),
            ],
        ),
    ]
