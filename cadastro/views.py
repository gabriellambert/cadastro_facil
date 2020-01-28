from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm


def index(request):
    pessoas = Pessoa.objects.all()
    dados = {
        'pessoas': pessoas,
    }
    return render(request, 'index.html', dados)

def pessoa_nova(request):
    if request.method == "POST":
        form = PessoaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PessoaForm()
    return render(request, 'pessoa_edit.html', {'form': form})


def pessoa_update(request, id):
    dados = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    dados['pessoa'] = pessoa
    dados['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        return render(request, 'pessoa_update.html', dados)

def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    dados = {
        'pessoa': pessoa,
    }
    if request.method == 'POST':
        pessoa.delete()
        return redirect('index')
    else:
        return render(request, 'confirmar_delete.html', dados)
