from django.db import models
import datetime
from dateutil.relativedelta import relativedelta

class Paciente(models.Model):
    id_paciente=models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    data_nascimento = models.DateTimeField()
    tutor=models.TextField(max_length=200)
    id_pelagem= models.ForeignKey('Pelagem',on_delete=models.CASCADE)
    veterinario_responsavel = models.ForeignKey('Veterinario',on_delete=models.CASCADE)
    data_castracao=models.DateTimeField(null=True, blank=True)    
    def idade(self):
        return relativedelta(datetime.datetime.now(),self.data_nascimento).years

class Pelagem(models.Model):
    id_pelagem=models.AutoField(primary_key=True)
    dsc_pelagem=models.TextField(max_length=200)

class Veterinario(models.Model):
    id_veterinario=models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    matricula=models.PositiveIntegerField()

class Procedimento(models.Model):
    id_procedimento=models.AutoField(primary_key=True)
    id_tpprocedimento=models.ForeignKey('TipoProcedimento',on_delete=models.CASCADE)
    data=models.DateTimeField()
    paciente=models.ForeignKey('Paciente',on_delete=models.CASCADE)
    veterinario = models.ForeignKey('Veterinario',on_delete=models.CASCADE)
    valor_procedimento=models.DecimalField(max_digits=8,decimal_places=2)

class TipoProcedimento(models.Model):
    id_tpprocedimento=models.AutoField(primary_key=True)
    nome_procedimento= models.TextField(max_length=200)

class Pagamento(models.Model):
    id_pagamento=models.AutoField(primary_key=True)
    id_procedimento=models.ForeignKey('Procedimento',on_delete=models.CASCADE)
    valor_pago=models.DecimalField(max_digits=8,decimal_places=2)
    