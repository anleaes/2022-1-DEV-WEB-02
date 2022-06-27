from django.db import models

# Create your models here.

class Disciplina(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    semestre = models.CharField('Semestre', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    codigod = models.CharField('CodigoD', max_length=10)
    carga = models.CharField('CargaHoraria', max_length=10)
    cursoss = models.CharField('Cursos', max_length=10)
    
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering =['id']

    def __str__(self):
        return self.name

