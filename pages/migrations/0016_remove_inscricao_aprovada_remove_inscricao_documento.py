# Generated by Django 4.0.5 on 2022-11-22 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_aluno_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscricao',
            name='aprovada',
        ),
        migrations.RemoveField(
            model_name='inscricao',
            name='documento',
        ),
    ]
