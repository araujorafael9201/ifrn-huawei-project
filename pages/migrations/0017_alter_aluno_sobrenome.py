# Generated by Django 4.0.5 on 2022-11-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_remove_inscricao_aprovada_remove_inscricao_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='sobrenome',
            field=models.CharField(default='', max_length=255),
        ),
    ]
