# Generated by Django 4.0.5 on 2022-06-08 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_aluno_do_ifrn_aluno_aluno_ifrn_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='servidor_do_ifrn',
            new_name='servidor_ifrn',
        ),
    ]
