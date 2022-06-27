from django.urls import path
from . import views

app_name = 'alunos'

urlpatterns = [
    path('', views.list_alunos, name='list_alunos'),
    path('adicionar/', views.add_aluno, name='add_aluno'),
    path('editar/<int:id_aluno>/', views.edit_aluno, name='edit_aluno'),
    path('excluir/<int:id_aluno>/', views.delete_aluno, name='delete_aluno'),
    path('buscar/', views.search_alunos, name='search_alunos'),

]