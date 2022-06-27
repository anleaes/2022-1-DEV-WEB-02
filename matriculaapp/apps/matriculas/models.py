from django.db import models

# Create your models here.
class Matricula(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    codigo = models.CharField('Codigo da matricula', max_length=50)
    tipo = models.TextField('Tipo', max_length=20) 
    data = models.TextField('Data', max_length=20) 
    aluno = models.TextField('alunos', max_length=20) 
    disciplina = models.TextField('disciplina', max_length=20) 
    
    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
        ordering =['id']

    def __str__(self):
        return self.name

