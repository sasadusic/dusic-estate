# Generated by Django 4.0.5 on 2022-07-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='House', max_length=200)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=40000.0, max_digits=10, null=True)),
                ('address', models.CharField(blank=True, default='123 Main St', max_length=200, null=True)),
                ('bathrooms', models.DecimalField(blank=True, decimal_places=1, default=2.0, max_digits=3, null=True)),
                ('bedrooms', models.DecimalField(blank=True, decimal_places=1, default=2, max_digits=3, null=True)),
                ('squares', models.DecimalField(blank=True, decimal_places=2, default=1000.0, max_digits=10, null=True)),
                ('description', models.TextField(blank=True, default='This single-family home in Austin has been upgraded with stainless steel appliances and features an open-concept layout.', null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
