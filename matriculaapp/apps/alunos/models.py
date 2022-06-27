from django.db import models
from django.db import models
from disciplinas.models import Disciplina

# Create your models here.

class Aluno(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    aluno_disciplina = models.ManyToManyField(Disciplina, through='AlunoDisciplina', blank=True)
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering =['id']

    def __str__(self):
        return self.first_name


class AlunoDisciplina(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    Disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item da Disciplina'
        verbose_name_plural = 'Itens da Disciplina'
        ordering =['id']

    def __str__(self):
        return self.disciplina.name
