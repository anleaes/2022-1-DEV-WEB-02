from django import forms
from .models import Order, Aluno, OrderItem , Disciplina

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        exclude = ('aluno', 'created_on' , 'updated_on')

class OrderItemForm(forms.ModelForm):
    
    class Meta:
        model = OrderItem
        exclude = ('order', 'created_on' , 'updated_on')
