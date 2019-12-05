from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    nascimento = models.CharField(max_length=8, null=False, blank=False)
    fone = models.CharField(max_length=11)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    #endereco = models.ForeignKey("Endereco", on_delete=models.PROTECT)


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=8)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
