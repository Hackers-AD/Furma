# Generated by Django 3.0.4 on 2020-03-22 16:45

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0006_auto_20200322_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefit_type', models.CharField(blank=True, choices=[('Percentage', "Discount is a percentage off of the product's value"), ('Fixed', "Discount is a fixed amount off of the product's value"), ('Multibuy', 'Discount is to give the cheapest product for free'), ('Fixed price', 'Get the products that meet the condition for a fixed price'), ('Shipping percentage', 'Discount is a percentage off of the shipping'), ('Shipping absolute', 'Discount is a fixed amount of the shipping cost'), ('Shipping fixed price', 'Get shipping for fixed price')], max_length=128)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('max_affected_items', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_type', models.CharField(blank=True, choices=[('Count', 'Depends on number of items in basket that are in condition range'), ('Value', 'Depends on value of items in basket that are in condition range'), ('Coverage', 'Needs to contain a set number of DISTINCT items  from condition range')], max_length=128)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_public', models.BooleanField(default=False)),
                ('includes_all_product', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('classes', models.ManyToManyField(blank=True, related_name='range_classes', to='catalogue.Product')),
                ('excluded_products', models.ManyToManyField(blank=True, related_name='excludes', to='catalogue.Product')),
                ('included_categories', models.ManyToManyField(blank=True, related_name='range_categories', to='catalogue.Product')),
                ('included_products', models.ManyToManyField(blank=True, related_name='includes', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ConditionalOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True)),
                ('offer_type', models.CharField(choices=[('Site', 'Site Offer-available to all user'), ('Voucher', 'Voucher offer-available only after entering voucher code'), ('User', 'User offer-available to certain types of users only'), ('Session', 'Session offer-temporary offer, available for the duration of session ')], default='Site', max_length=128)),
                ('exclusive', models.BooleanField(default=True)),
                ('status', models.CharField(default='open', max_length=64)),
                ('priority', models.IntegerField(db_index=True, default=0)),
                ('start_datetime', models.DateTimeField(blank=True, null=True)),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('max_global_applications', models.PositiveIntegerField(blank=True, null=True)),
                ('max_user_applications', models.PositiveIntegerField(blank=True, null=True)),
                ('max_basket_applications', models.PositiveIntegerField(blank=True, null=True)),
                ('max_discount', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=12, null=True)),
                ('total_discount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12)),
                ('num_applications', models.PositiveIntegerField(default=0)),
                ('num_orders', models.PositiveIntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offer_benefit', to='offers.Benefit')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='offers.Condition')),
            ],
        ),
        migrations.AddField(
            model_name='condition',
            name='range',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='offers.Range'),
        ),
        migrations.AddField(
            model_name='benefit',
            name='range',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='offers.Range'),
        ),
    ]
