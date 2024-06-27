from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Pessoa,Cargos


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/index.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        pessoa = Pessoa(nome = nome, email = email, senha = senha)

        pessoa.save()

        return HttpResponse('Registrado com Sucesso')
    
def listar(request):
    
    cargo_2 = Cargos.objects.get(id = 2)

    pessoa = Pessoa.objects.get(id = 6)
    pessoa.cargos.add(cargo_2)
    pessoa.save()

    pessoas = Pessoa.objects.all()

    return render(request, 'listar/listar.html', {'pessoas': pessoas})