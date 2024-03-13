from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    doenca = models.CharField(max_length=100)
    idade = models.IntegerField()
    naturalidade = models.CharField(max_length=100)
    onde_mora = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Doenca(models.Model):
    nome = models.CharField(max_length=100)
    sintomas = models.TextField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome
