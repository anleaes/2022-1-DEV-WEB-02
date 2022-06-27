from django.shortcuts import render, get_object_or_404, redirect
from .forms import MatriculaForm
from .models import Matricula

# Create your views here.

def add_matricula(request):
    template_name = 'matriculas/add_matricula.html'
    context = {}
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('matriculas:list_matriculas')
    form = MatriculaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_matriculas(request):
    template_name = 'matriculas/list_matriculas.html'
    matriculas = Matricula.objects.filter()
    context = {
        'matriculas': matriculas
    }
    return render(request, template_name, context)

def edit_matricula(request, id_matricula):
    template_name = 'matriculas/add_matricula.html'
    context ={}
    matricula = get_object_or_404(Matricula, id=id_matricula)
    if request.method == 'POST':
        form = MatriculaForm(request.POST, instance=matricula)
        if form.is_valid():
            form.save()
            return redirect('matriculas:list_matriculas')
    form = MatriculaForm(instance=matricula)
    context['form'] = form
    return render(request, template_name, context)

def delete_matricula(request, id_matricula):
    matricula = Matricula.objects.get(id=id_matricula)
    matricula.delete()
    return redirect('matriculas:list_matriculas')
