# Generated by Django 5.0.6 on 2024-06-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_alter_aluno_id_alter_curso_id_alter_matricula_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default='', max_length=11),
        ),
    ]
