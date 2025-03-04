from django.db import models

class Curso(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    carga_horaria = models.IntegerField('Carga Horária')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        def __str__(self):
            return self.nome

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)

    class Meta:
        abstract = True
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        def __str__(self):
            return self.nome


class Professor(Pessoa):
    OPCOES = (
        ('Doutorado',       'Doutorado'),
        ('Mestrado',        'Mestrado'),
        ('Especialização',  'Especialização'),
        ('Graduação',       'Graduação'),
    )
    titulacao = models.CharField('Titulação', blank=True, max_length=100, choices=OPCOES)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

class Aluno(Pessoa):
    matricula = models.IntegerField('Matrícula', unique=True)
    data_nascimento = models.DateField('Data de Nascimento', blank=True, null=True, help_text='Formato DD/MM/AAAA')
    email = models.EmailField('E-mail', blank=True, max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'


class Disciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    carga_horaria = models.IntegerField('Carga horária')
    obrigatoria = models.BooleanField('Obrigatória', default=True)
    ementa = models.TextField('Ementa', blank=True, max_length=500)
    bibliografia = models.TextField('Bibliografia', blank=True, max_length=500)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        def __str__(self):
            return self.nome

class Turma(models.Model):
    ano = models.IntegerField('Ano')
    semestre = models.IntegerField('Semestre')
    turma = models.CharField('Turma', max_length=10)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, null=True, on_delete=models.SET_NULL)
    alunos = models.ManyToManyField(Aluno)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        def __str__(self):
            return f"{self.ano} / {self.semestre} / {self.turma} / {self.disciplina}"

