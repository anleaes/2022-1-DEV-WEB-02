from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoryForm
from .models import Category

# Create your views here.

def add_category(request):
    template_name = 'cursos/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('cursos:list_cursos')
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)

def list_cursos(request):
    template_name = 'cursos/list_cursos.html'
    cursos = Category.objects.filter()
    context = {
        'cursos': cursos
    }
    return render(request, template_name, context)

def edit_category(request, id_category):
    template_name = 'cursos/add_category.html'
    context ={}
    category = get_object_or_404(Category, id=id_category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('cursos:list_cursos')
    form = CategoryForm(instance=category)
    context['form'] = form
    return render(request, template_name, context)

def delete_category(request, id_category):
    category = Category.objects.get(id=id_category)
    category.delete()
    return redirect('cursos:list_cursos')
