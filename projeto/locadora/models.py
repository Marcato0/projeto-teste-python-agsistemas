from django.db import models


class Veiculo(models.Model):


    placa = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    veiculo = models.CharField(max_length=255)
    troca_oleo = models.IntegerField()
    

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.placa

class Motorista(models.Model):

    
    nome = models.CharField(max_length=255)
    fone = models.CharField(max_length=14)
    cnh = models.CharField(max_length=255)
    

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Controle(models.Model):

    
    veiculo = models.ForeignKey(Veiculo, on_delete=models.DO_NOTHING)
    motorista = models.ForeignKey(Motorista, on_delete=models.DO_NOTHING)
    data_saida = models.CharField(max_length=255)
    hora_saida = models.CharField(max_length=255)
    km_saida = models.IntegerField()
    destino = models.CharField(max_length=255)
    data_retorno = models.CharField(max_length=255)
    hora_retorno = models.CharField(max_length=255)
    km_retorno = models.IntegerField()
    km_percorrido = models.IntegerField()
    

   
