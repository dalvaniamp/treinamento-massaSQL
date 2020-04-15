from django.db import models

class Tutor(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Nome",max_length=200)
    cpf=models.CharField(unique=True, max_length=14)

class Patient(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Nome",max_length=200)
    birth_date = models.DateTimeField(verbose_name="Data de Nascimento",)
    tutor=models.ForeignKey('Tutor',on_delete=models.CASCADE)
    coat= models.ForeignKey('Coat',on_delete=models.CASCADE)
    veterinarian = models.ForeignKey('Veterinarian',on_delete=models.CASCADE)
    castration_date=models.DateTimeField(verbose_name="Data de Castração",null=True, blank=True)    

class Coat(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=200)

class Veterinarian(models.Model):
    id=models.AutoField(primary_key=True)
    name= models.TextField(max_length=200)
    registry=models.PositiveIntegerField()

class Procedure(models.Model):
    id=models.AutoField(primary_key=True)
    id_tpprocedimento=models.ForeignKey('ProcedureType',on_delete=models.CASCADE)
    data=models.DateTimeField()
    patient=models.ForeignKey('Patient',on_delete=models.CASCADE)
    veterinario = models.ForeignKey('Veterinarian',on_delete=models.CASCADE)
    valor_procedimento=models.DecimalField(max_digits=8,decimal_places=2)

class ProcedureType(models.Model):
    id=models.AutoField(primary_key=True)
    name= models.TextField(max_length=200)

class Payment(models.Model):
    id=models.AutoField(primary_key=True)
    procedure=models.ForeignKey('Procedure',on_delete=models.CASCADE)
    value=models.DecimalField(max_digits=8,decimal_places=2) 