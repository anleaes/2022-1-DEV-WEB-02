# Generated by Django 3.2.5 on 2022-06-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='aluno',
            field=models.TextField(max_length=20, verbose_name='alunos'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='data',
            field=models.TextField(max_length=20, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='disciplina',
            field=models.TextField(max_length=20, verbose_name='disciplina'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='tipo',
            field=models.TextField(max_length=20, verbose_name='Tipo'),
        ),
    ]