from ast import Delete
from turtle import title
from django.shortcuts import redirect, render , get_object_or_404 , redirect
from django.http import HttpResponse
from.forms import VeiculoForm
from.forms import MotoristaForm
from.forms import ControleForm
from django.contrib import messages
from django.core.paginator import Paginator 

from locadora.models import Veiculo
from locadora.models import Motorista
from locadora.models import Controle


def veiculosList(request):

    search = request.GET.get('search')
    if search:
        veiculos = Veiculo.objects.filter(placa__icontains=search)
        

    else:
        veiculos_list = Veiculo.objects.all()

        paginator = Paginator(veiculos_list , 3)
        page = request.GET.get('page')
        veiculos = paginator.get_page(page)

    return render (request, 'tasks/listaVeiculo.html'  , {'veiculos':veiculos})



# def veiculosView(request, id):
#     veiculo = get_object_or_404(Veiculo, pk = id)
#     return render(request, 'tasks/veiculos.html' , {'veiculo': veiculo})


def newVeiculo(request):

    if request.method == 'POST':
        formulario_do_veiculo = VeiculoForm(request.POST)

        if formulario_do_veiculo.is_valid():
            veiculos = formulario_do_veiculo.save(commit='True')
            return redirect ('/listaVeiculo')

    else:
        formulario_do_veiculo = VeiculoForm()
        return render(request, 'tasks/cadastroVeiculo.html' , {'form': formulario_do_veiculo})

def editVeiculo(request, id):
    edveiculo = get_object_or_404(Veiculo , pk=id)
    formulario_do_veiculo = VeiculoForm(instance = edveiculo)

    if (request.method == 'POST'):
        formulario_do_veiculo = VeiculoForm(request.POST , instance = edveiculo)

        if formulario_do_veiculo.is_valid():
            edveiculo.save()
            return redirect ('/listaVeiculo')

    else:
        return render(request, 'tasks/editVeiculos.html' ,{'form': formulario_do_veiculo ,'edveiculo':edveiculo })

def deleteVeiculo(request, id):
    delveiculo = get_object_or_404(Veiculo , pk=id)
    delveiculo.delete()
    messages.info(request, 'Registro Deletado Com Sucesso')
    return redirect ('/listaVeiculo')





def motoristasList(request):
#   motoristas = Motorista.objects.all()
#   return render (request, 'tasks/listaMotorista.html'  , {'motoristas':motoristas})

    search = request.GET.get('search')
    if search:
        motoristas = Motorista.objects.filter(nome__icontains=search)
        

    else:
        motorista_list = Motorista.objects.all()

        paginator = Paginator(motorista_list , 3)
        page = request.GET.get('page')
        motoristas = paginator.get_page(page)

    return render (request, 'tasks/listaMotorista.html'  , {'motorista':motoristas})

# def motoristasView(request, id):
#     motorista = get_object_or_404(Motorista, pk = id)
#     return render(request, 'tasks/motorista.html' , {'motorista': motorista})

def newMotorista(request):

    if request.method == 'POST':
        formulario_do_motorista = MotoristaForm(request.POST)

        if formulario_do_motorista.is_valid():
            motoristas = formulario_do_motorista.save(commit='True')
            return redirect ('/listaMotorista')

    else:
        formulario_do_motorista = MotoristaForm()
        return render(request, 'tasks/cadastroMotorista.html' , {'form': formulario_do_motorista})

def editMotorista(request, id):
    edmotorista = get_object_or_404(Motorista , pk=id)
    formulario_do_motorista = MotoristaForm(instance = edmotorista)

    if (request.method == 'POST'):
        formulario_do_motorista = MotoristaForm(request.POST , instance = edmotorista)

        if formulario_do_motorista.is_valid():
            edmotorista.save()
            return redirect ('/listaMotorista')

    else:
        return render(request, 'tasks/editMotoristas.html' ,{'form': formulario_do_motorista ,'edmotorista':edmotorista })

def deleteMotorista(request, id):
    delmotorista = get_object_or_404(Motorista , pk=id)
    delmotorista.delete()
    messages.info(request, 'Registro Deletado Com Sucesso')
    return redirect ('/listaMotorista')

# def principalList(request):
#   return render (request, 'tasks/index.html')



def newControle(request):

    if request.method == 'POST':
        formulario_do_controle = ControleForm(request.POST)

        if formulario_do_controle.is_valid():
            controle = formulario_do_controle.save(commit='True')
            return redirect ('/')

    else:
        formulario_do_controle = ControleForm()
        return render(request, 'tasks/cadastroControle.html' , {'form': formulario_do_controle})

def controleList(request):

    search = request.GET.get('search')
    if search:
        controle = Controle.objects.filter( data_saida__icontains=search)
        

    else:
        controle_list = Controle.objects.all()

        paginator = Paginator(controle_list , 3)
        page = request.GET.get('page')
        controle = paginator.get_page(page)

    return render (request, 'tasks/index.html'  , {'controle':controle})


def editControle(request, id):
    edcontrole = get_object_or_404(Controle , pk=id)
    formulario_do_controle = ControleForm(instance = edcontrole)

    if (request.method == 'POST'):
        formulario_do_controle = ControleForm(request.POST , instance = edcontrole)

        if formulario_do_controle.is_valid():
            edcontrole.save()
            return redirect ('/')

    else:
        return render(request, 'tasks/editControle.html' ,{'form': formulario_do_controle ,'edcontrole':edcontrole })

def deleteControle(request, id):
    delcontrole = get_object_or_404(Controle , pk=id)
    delcontrole.delete()
    messages.info(request, 'Registro Deletado Com Sucesso')
    return redirect ('/')    