from django.shortcuts import render, get_object_or_404, redirect
from .forms import DisciplinaForm
from .models import Disciplina

# Create your views here.

def add_disciplina(request):
    template_name = 'disciplinas/add_disciplina.html'
    context = {}
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('disciplinas:list_disciplinas')
    form = DisciplinaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_disciplinas(request):
    template_name = 'disciplinas/list_disciplinas.html'
    disciplinas = Disciplina.objects.filter()
    context = {
        'disciplinas': disciplinas
    }
    return render(request, template_name, context)

def edit_disciplina(request, id_disciplina):
    template_name = 'disciplinas/add_disciplina.html'
    context ={}
    disciplina = get_object_or_404(Disciplina, id=id_disciplina)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('disciplinas:list_disciplinas')
    form = DisciplinaForm(instance=disciplina)
    context['form'] = form
    return render(request, template_name, context)

def delete_disciplina(request, id_disciplina):
    disciplina = Disciplina.objects.get(id=id_disciplina)
    disciplina.delete()
    return redirect('disciplinas:list_disciplinas')
