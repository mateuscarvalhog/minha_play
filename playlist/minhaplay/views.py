from django.shortcuts import render, redirect
from .models import Faixa
from .form import FaixaForm
from itertools import chain

# Create your views here.

def createFaixa(request):
    data = {}
    form = FaixaForm(request.POST or None)
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('readFaixa')
    
    return render(request, 'minhaplay/createFaixa.html', data)

def readFaixa(request):
    data = {}
    
    if request.method == "POST":
        search = request.POST['search_faixa']
        if search != "":
            names = Faixa.objects.filter(nome=search)
            artists = Faixa.objects.filter(artista=search)
            result_list = list(chain(names, artists))
            data['Faixas'] = result_list

            return render(request, 'minhaplay/readFaixa.html', data)
    
    data['Faixas'] = Faixa.objects.all()

    return render(request, 'minhaplay/readFaixa.html', data)

def updateFaixa(request, pk):
    updatedFaixa = Faixa.objects.get(pk=pk)
    form = FaixaForm(request.POST or None, instance=updatedFaixa)
    
    data = {}
    data['form'] = form
    data['faixa'] = updatedFaixa

    if form.is_valid():
        form.save()
        return redirect('readFaixa')

    return render(request, 'minhaplay/updateFaixa.html', data)

def deleteFaixa(request, pk):
    deletedFaixa = Faixa.objects.get(pk=pk)
    deletedFaixa.delete()

    return redirect('readFaixa')

def showLetra(request, pk):
    faixa = Faixa.objects.get(pk=pk)
    data = {}
    data['faixa'] = faixa

    return render(request, 'minhaplay/showLetra.html', data)