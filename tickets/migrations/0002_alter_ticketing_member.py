# Generated by Django 4.0 on 2023-07-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketing',
            name='member',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
