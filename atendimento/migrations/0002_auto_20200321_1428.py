# Generated by Django 3.0.4 on 2020-03-21 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('questionario', '0001_initial'),
        ('funcionario', '0002_funcionario_dtnascimento'),
        ('atendimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='cliente.Cliente', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='funcionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to='funcionario.Funcionario', verbose_name='Funcionário'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='questionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionario', to='questionario.Questionario', verbose_name='Questionário'),
        ),
    ]
