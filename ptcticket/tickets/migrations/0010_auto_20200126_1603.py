# Generated by Django 3.0.2 on 2020-01-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_auto_20200126_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='course',
            field=models.CharField(choices=[('CSCE 111', 'CSCE 111'), ('CSCE 121', 'CSCE 121'), ('CSCE 206', 'CSCE 206'), ('CSCE 221', 'CSCE 221'), ('CSCE 222', 'CSCE 222'), ('CSCE 312', 'CSCE 312'), ('CSCE 313', 'CSCE 313'), ('CSCE 314', 'CSCE 314'), ('CSCE 315', 'CSCE 315'), ('Other', 'Other')], max_length=8),
        ),
    ]
