# Generated by Django 4.0.2 on 2022-04-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterBottle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=300)),
                ('Brand', models.CharField(max_length=300)),
                ('Cost', models.DecimalField(decimal_places=2, max_digits=2)),
                ('Size', models.CharField(max_length=300)),
                ('MouthSize', models.CharField(max_length=300)),
                ('Color', models.CharField(max_length=300)),
                ('Current_Quantity', models.IntegerField(max_length=300)),
            ],
        ),
    ]