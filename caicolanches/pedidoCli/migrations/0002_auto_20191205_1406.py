# Generated by Django 3.0 on 2019-12-05 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidoCli', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nascimento',
            field=models.CharField(max_length=8),
        ),
    ]
