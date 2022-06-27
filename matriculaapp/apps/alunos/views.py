from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlunoForm
from .models import Aluno, Disciplina, AlunoDisciplina

# Create your views here.

def add_aluno(request):
    template_name = 'alunos/add_aluno.html'
    context = {}
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('alunos:list_alunos')
    form = AlunoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_alunos(request):
    template_name = 'alunos/list_alunos.html'
    aluno_disciplinas = AlunoDisciplina.objects.filter()
    disciplinas = Disciplina.objects.filter()
    alunos = Aluno.objects.filter()
    context = {
        'alunos': alunos,
        'disciplinas': disciplinas,
        'aluno_disciplinas': aluno_disciplinas
    }
    return render(request, template_name, context)

def edit_aluno(request, id_aluno):
    template_name = 'alunos/add_aluno.html'
    context ={}
    aluno = get_object_or_404(Aluno, id=id_aluno)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('alunos:list_alunos')
    form = AlunoForm(instance=aluno)
    context['form'] = form
    return render(request, template_name, context)

def delete_aluno(request, id_aluno):
    aluno = Aluno.objects.get(id=id_aluno)
    aluno.delete()
    return redirect('alunos:list_alunos')

def search_alunos(request):
    template_name = 'alunos/list_alunos.html'
    query = request.GET.get('query')
    aluno_disciplinas = AlunoDisciplina.objects.filter()
    disciplinas = Disciplina.objects.filter()
    alunos = Aluno.objects.filter(last_name__icontains=query)
    context = {
        'alunos': alunos,
        'disciplinas': disciplinas,
        'aluno_disciplinas': aluno_disciplinas
    }
    return render(request,template_name, context)
