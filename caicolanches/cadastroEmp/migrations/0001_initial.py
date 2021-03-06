# Generated by Django 2.2.7 on 2019-12-04 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=8)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeFrant', models.CharField(max_length=150)),
                ('social', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=11, unique=True)),
                ('fone', models.CharField(max_length=11)),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('responsavel', models.CharField(max_length=150)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastroEmp.Endereco')),
            ],
        ),
    ]
