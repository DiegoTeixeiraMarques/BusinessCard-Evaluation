# Generated by Django 3.0.4 on 2020-03-21 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('funcionario', '0002_funcionario_dtnascimento'),
        ('questionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.BigIntegerField(unique=True, verbose_name='Atendimento')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='cliente.Cliente', verbose_name='Cliente')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to='funcionario.Funcionario', verbose_name='Funcionário')),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionario', to='questionario.Questionario', verbose_name='Questionário')),
            ],
            options={
                'verbose_name': 'Atendimento',
                'verbose_name_plural': 'Atendimentos',
            },
        ),
    ]