# Generated by Django 4.0.5 on 2022-11-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_remove_aluno_aluno_ifrn_remove_aluno_celular_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
    ]
