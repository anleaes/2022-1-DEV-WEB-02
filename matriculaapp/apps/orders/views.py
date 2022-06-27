from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm, OrderItemForm
from .models import Order , OrderItem, Disciplina, Aluno

# Create your views here.

def add_order(request, id_aluno):
    template_name = 'orders/add_order.html'
    context = {}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.aluno = Aluno.objects.get(id=id_aluno)
            f.save()
            form.save_m2m()
            return redirect('orders:list_orders')
    form = OrderForm()
    context['form'] = form
    return render(request, template_name, context)

def list_orders(request):
    template_name = 'orders/list_orders.html'
    orders = Order.objects.filter()
    order_items = OrderItem.objects.filter()
    disciplinas = Disciplina.objects.filter()
    alunos = Aluno.objects.filter()
    context = {
        'orders': orders,
        'order_items': order_items,
        'disciplinas': disciplinas,
        'alunos': alunos
    }
    return render(request, template_name, context)

def delete_order(request, id_order):
    order = Order.objects.get(id=id_order)
    order.delete()
    return redirect('orders:list_orders')

def add_order_item(request, id_order):
    template_name = 'orders/add_order_item.html'
    context = {}
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.order = Order.objects.get(id=id_order)
            f.save()
            form.save_m2m()
            return redirect('orders:list_orders')
    form = OrderItemForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_order_item(request, id_order_item):
    orderitem = OrderItem.objects.get(id=id_order_item)
    orderitem.delete()
    return redirect('orders:list_orders')

def edit_order_status(request, id_order):
    template_name = 'orders/edit_order_status.html'
    context ={}
    order = get_object_or_404(Order, id=id_order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:list_orders')
    form = OrderForm(instance=order)
    context['form'] = form
    return render(request, template_name, context)

