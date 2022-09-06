# Generated by Django 2.2.19 on 2022-09-06 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('matricula', models.IntegerField(unique=True, verbose_name='Matrícula')),
                ('data_nascimento', models.DateField(blank=True, help_text='Formato DD/MM/AAAA', null=True, verbose_name='Data de Nascimento')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='E-mail')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Curso')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga horária')),
                ('obrigatoria', models.BooleanField(default=True, verbose_name='Obrigatória')),
                ('ementa', models.TextField(blank=True, max_length=500, verbose_name='Ementa')),
                ('bibliografia', models.TextField(blank=True, max_length=500, verbose_name='Bibliografia')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.Curso')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('titulacao', models.CharField(blank=True, choices=[('Doutorado', 'Doutorado'), ('Mestrado', 'Mestrado'), ('Especialização', 'Especialização'), ('Graduação', 'Graduação')], max_length=100, verbose_name='Titulação')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.Curso')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(verbose_name='Ano')),
                ('semestre', models.IntegerField(verbose_name='Semestre')),
                ('turma', models.CharField(max_length=10, verbose_name='Turma')),
                ('alunos', models.ManyToManyField(to='aplic.Aluno')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.Disciplina')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.Professor')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
    ]
