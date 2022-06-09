# Generated by Django 4.0.5 on 2022-06-09 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_rename_servidor_do_ifrn_aluno_servidor_ifrn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='curso',
        ),
        migrations.AddField(
            model_name='turma',
            name='nome_do_curso',
            field=models.CharField(default='Curso', max_length=255),
        ),
        migrations.AlterField(
            model_name='professor',
            name='turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.turma'),
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.aluno')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.turma')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.FileField(upload_to='uploads')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.aluno')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.turma')),
            ],
        ),
    ]
