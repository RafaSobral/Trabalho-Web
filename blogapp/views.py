from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .forms import ArtigoForm
from .models import Artigo
from datetime import datetime


# Create your views here.

def home(request):
    artigos = Artigo.objects.all()
    ultimos_artigos = Artigo.objects.order_by('data_publicacao')[:5]
    return render(request, 'home.html', {'artigos': artigos, 'ultimos_artigos': ultimos_artigos})


def artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return render(request, 'artigo.html', {'artigo': artigo}) 

@login_required(login_url="/login/")
def configuracoes(request):
    artigos = Artigo.objects.all()
    return render(request, 'configuracoes.html', {'artigos': artigos})

@login_required(login_url="/login/")
def adicionar(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES)
        data_atual = datetime.now()  
        if form.is_valid():
            form.save()
            return render(request, 'adicionar.html', {'form': form, 'artigo': artigo, 'data_atual': data_atual})
    else:
        form = ArtigoForm()
        data_atual = datetime.now()  
        return render(request, 'adicionar.html', {'form': form, 'data_atual': data_atual})

@login_required(login_url="/login/")
def editar(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.method == "POST":
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()  
            return redirect('configuracoes')  
    else:
        form = ArtigoForm(instance=artigo)
        data_atual = datetime.now() 
    return render(request, 'editar.html', {'form': form, 'artigo': artigo, 'data_atual': data_atual})


@login_required(login_url="/login/")
def deletar(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    artigo.delete()
    return redirect('configuracoes')


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha )
        if user:
            login_django(request, user)
            return redirect('configuracoes')
        else:
            return HttpResponse("Email ou senha invalidos")




        

