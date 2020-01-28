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
