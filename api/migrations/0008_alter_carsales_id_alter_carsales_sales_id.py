# Generated by Django 4.0.6 on 2022-07-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_carsales_id_alter_carsales_sales_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsales',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='carsales',
            name='sales_id',
            field=models.IntegerField(),
        ),
    ]
