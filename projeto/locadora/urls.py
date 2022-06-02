from django.urls import path

from.import views

urlpatterns = [
    

    path('listaVeiculo' , views.veiculosList , name='veiculo-list'),
    # path('tasks/<int:id>', views.veiculosView , name='veiculos-view'),
    path('cadastroVeiculo' , views.newVeiculo, name='new-veiculo'),
    path('editVeiculo/<int:id>' , views.editVeiculo, name='edit-veiculo'),
    path('deleteVeiculo/<int:id>' , views.deleteVeiculo, name='delete-veiculo'),

    path('listaMotorista' , views.motoristasList , name='motorista-list'),
    # path('motorista/<int:id>', views.motoristasView , name='motoristas-view'),
    path('cadastroMotorista' , views.newMotorista, name='new-veiculo'),
    path('editMotorista/<int:id>' , views.editMotorista, name='edit-motorista'),
    path('deleteMotorista/<int:id>' , views.deleteMotorista, name='delete-motorista'),

    # path('' , views.principalList , name='principal-list'),
    

     path('' , views.controleList , name='controle-list'),
     path('cadastroControle' , views.newControle, name='new-controle'),
     path('editControle/<int:id>' , views.editControle, name='edit-controle'),
     path('deleteControle/<int:id>' , views.deleteControle, name='delete-controle'),
]