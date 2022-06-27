from django import forms
from .models import Matricula

class MatriculaForm(forms.ModelForm):

    class Meta:
        model = Matricula
        exclude = ('created_on' , 'updated_on',)
