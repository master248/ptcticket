# Generated by Django 3.0.2 on 2020-01-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_tickets_peer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='peer',
            field=models.CharField(default='none', max_length=50, null=True),
        ),
    ]
