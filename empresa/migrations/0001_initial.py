# Generated by Django 3.0.4 on 2020-03-19 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cnpj', models.CharField(max_length=14, unique=True, verbose_name='CNPJ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=' Criado em ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=' Atualizado em ')),
            ],
            options={
                'verbose_name': 'Cooperativa',
                'verbose_name_plural': 'Cooperativas',
            },
        ),
    ]
