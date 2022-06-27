from django.urls import path
from . import views

app_name = 'disciplinas'

urlpatterns = [
    path('', views.list_disciplinas, name='list_disciplinas'),
    path('adicionar/', views.add_disciplina, name='add_disciplina'),
    path('editar/<int:id_disciplina>/', views.edit_disciplina, name='edit_disciplina'),
    path('excluir/<int:id_disciplina>/', views.delete_disciplina, name='delete_disciplina'),
]