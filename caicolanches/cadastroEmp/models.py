from django.db import models

# Create your models here.
class Estabelecimento(models.Model):
    nomeFrant=models.CharField(max_length=150)
    social=models.CharField(max_length=255)
    cnpj=models.CharField(max_length=11,unique=True)
    fone=models.CharField(max_length=11)
    login=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    endereco=models.ForeignKey("Endereco", on_delete=models.PROTECT)
    responsavel=models.CharField(max_length=150)

class Endereco(models.Model):
    rua=models.CharField(max_length=100)
    bairro=models.CharField(max_length=100)
    numero=models.CharField(max_length=8)
    cidade=models.CharField(max_length=100)
    estado=models.CharField(max_length=100)
    cep=models.CharField(max_length=8)

    def __str__(self):
        return self.rua