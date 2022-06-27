from django.urls import path
from . import views

app_name = 'matriculas'

urlpatterns = [
    path('', views.list_matriculas, name='list_matriculas'),
    path('adicionar/', views.add_matricula, name='add_matricula'),
    path('editar/<int:id_matricula>/', views.edit_matricula, name='edit_matricula'),
    path('excluir/<int:id_matricula>/', views.delete_matricula, name='delete_matricula'),
]
