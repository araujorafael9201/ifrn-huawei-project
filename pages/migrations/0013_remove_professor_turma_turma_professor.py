# Generated by Django 4.0.5 on 2022-10-18 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_aula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='turma',
        ),
        migrations.AddField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.professor'),
        ),
    ]